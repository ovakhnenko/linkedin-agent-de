#!/usr/bin/env python3
"""
detect.py - a five-check panel that scores how machine-written a GERMAN draft looks.

German edition. Same five checks as the English original, re-tuned for German:
  - sentence splitting ignores abbreviations (z. B., d. h., bzw.) and ordinals (3. März)
  - SPECIFICITY cannot use capitalised words as "names" (German capitalises every
    noun), so it counts numbers, money, percentages, acronyms (SAP, KMU),
    brand-style CamelCase (LinkedIn, PowerShell), weekdays/months and @mentions
  - VOICE counts colloquial markers instead of English contractions: gibt's,
    hab, 'ne, nix plus modal particles (halt, eben, mal, ja, doch, eh, wohl),
    which humans use far more than models; plus du/ihr/ich/wir pronouns

What this is NOT: GPTZero, Originality, Copyleaks, Winston or Turnitin.
It does not call their APIs and it cannot promise their verdict.

Usage
  python3 detect.py draft.txt
  python3 detect.py draft.txt --json
  python3 detect.py before.txt after.txt      # compare two drafts
"""

import argparse
import json
import os
import re
import statistics
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop.json")

SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")
WORD_RE = re.compile(r"[^\W\d_]+(?:'[^\W\d_]+)?")
ABBR_RE = re.compile(
    r"\b(?:z\.\s?B|d\.\s?h|u\.\s?a|o\.\s?ä|u\.\s?U|s\.\s?o|s\.\s?u|i\.\s?d\.\s?R|"
    r"bzw|ca|ggf|usw|etc|Nr|Dr|Prof|inkl|exkl|evtl|vgl|zzgl|bspw|sog|max|min|"
    r"Mio|Mrd|Tsd|Std|Min|Jh|Abs|Str|Tel)\.",
    re.IGNORECASE)
ORDINAL_RE = re.compile(
    r"(\d)\.(?=\s+(?:[a-zäöüß]|Januar|Februar|März|April|Mai|Juni|Juli|August|"
    r"September|Oktober|November|Dezember|Jan|Feb|Mär|Apr|Jun|Jul|Aug|Sep|Okt|Nov|Dez)\b)")
MASK = "⁣"
# Colloquial German: apostrophe contractions, clipped forms, modal particles.
COLLOQUIAL = re.compile(
    r"\b\w+'s\b|'n\b|'ne\b|\b(?:hab|habs|nen|ne|nix|nich|grad|isses|gibts|gehts|"
    r"haste|biste|kannste|weißte|halt|eben|mal|eh|ja|doch|wohl|ruhig|bloß|echt|"
    r"krass|klar|okay|ok)\b",
    re.IGNORECASE)
PRONOUNS = re.compile(
    r"\b(?:ich|mich|mir|mein\w*|wir|uns|unser\w*|du|dich|dir|dein\w*|ihr|euch|euer|eure\w*)\b",
    re.IGNORECASE)
FORMAL_YOU = re.compile(r"(?<=[a-zäöüß,] )(?:Sie|Ihnen|Ihr\w*)\b")
NUMBERS = re.compile(r"\d[\d.,]*")
CONCRETE = re.compile(
    r"\b[A-ZÄÖÜ]{2,}\d*\b"                       # acronyms: SAP, KMU, B2B
    r"|\b[A-Za-z]*[a-z][A-Z]\w*\b"               # CamelCase brands: LinkedIn, iPhone
    r"|\b\w*\d\w*[A-Za-z]\w*\b"                  # mixed tokens: Q3, S4HANA
    r"|@\w+"                                     # mentions
    r"|\b(?:Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag|Januar|Februar|"
    r"März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\b"
    r"|[€$]")


def mask_abbr(text):
    text = ABBR_RE.sub(lambda m: m.group(0).replace(".", MASK), text)
    return ORDINAL_RE.sub(lambda m: m.group(1) + MASK, text)


def clamp(n):
    return max(0.0, min(100.0, n))


def scale(value, human, machine):
    """Map value onto 0-100 where `human` -> 100 and `machine` -> 0."""
    if human == machine:
        return 50.0
    return clamp((value - machine) / (human - machine) * 100)


def sentences(text):
    return [s.strip() for s in SENT_RE.findall(mask_abbr(text)) if len(s.split()) > 2]


def words(text):
    return WORD_RE.findall(text)


ADJ_SUFFIX = r"(?:e[mnrs]?|er(?:e[mnrs]?)?|st(?:e[mnrs]?)?)?"


def lex_pattern(find, family=""):
    stem = find.endswith("*")
    core = find[:-1] if stem else find
    body = re.escape(core).replace(r"\ ", r"\s+")
    left = r"\b" if core[:1].isalnum() else r"(?<!\w)"
    if stem:
        # Adjectives: only inflection endings, so robust* never hits "Robustheit".
        suffix = ADJ_SUFFIX if family == "adjectives" else r"\w*"
        return re.compile(left + "(" + body + ")(" + suffix + r")\b", re.IGNORECASE)
    right = r"\b" if core[-1:].isalnum() else ""
    return re.compile(left + "(" + body + ")" + right, re.IGNORECASE)


def check_burstiness(text):
    """Humans vary sentence length hard. Models write even."""
    lens = [len(s.split()) for s in sentences(text)]
    if len(lens) < 4:
        return 50.0, "too short to judge"
    mean = statistics.mean(lens)
    cv = statistics.pstdev(lens) / mean if mean else 0
    score = scale(cv, human=0.70, machine=0.22)
    return score, f"variation {cv:.2f} across {len(lens)} sentences (want 0.55+)"


def check_specificity(text):
    """Numbers, names and concrete nouns. Slop is abstract."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "too short to judge"
    per100 = 100 / len(w)
    hits = len(NUMBERS.findall(text)) + len(set(CONCRETE.findall(text)))
    density = hits * per100
    score = scale(density, human=4.5, machine=0.3)
    return score, f"{hits} concrete markers, {density:.1f} per 100 words (want 3+)"


def check_slop(text, lex):
    """Stock vocabulary density against the lexicon."""
    w = words(text)
    if not w:
        return 50.0, "empty"
    hits, found = 0, []
    for entry in lex["words"] + lex["phrases"]:
        pattern = lex_pattern(entry["find"], entry["family"])
        n = len(pattern.findall(text))
        if n:
            hits += n
            found.append(entry["find"])
    density = hits * 100 / len(w)
    score = scale(density, human=0.0, machine=4.0)
    detail = f"{hits} stock terms, {density:.1f} per 100 words"
    if found:
        detail += " (" + ", ".join(sorted(found)[:4]) + (", ..." if len(found) > 4 else "") + ")"
    return score, detail


def check_fingerprint(text):
    """Characters a phone keyboard does not produce."""
    invisible = sum(1 for c in text if unicodedata.category(c) == "Cf")
    em = text.count("—")
    curly = sum(text.count(c) for c in "‘’“”„‚»«")
    ellip = text.count("…")
    nbsp = sum(text.count(c) for c in "   ")
    total = invisible * 4 + em * 2 + curly + ellip + nbsp
    per1k = total * 1000 / max(len(text), 1)
    score = scale(per1k, human=0.0, machine=12.0)
    detail = (f"{invisible} invisible, {em} em dash, {curly} curly quote, "
              f"{ellip} ellipsis, {nbsp} hard space")
    return score, detail


def check_voice(text, lex):
    """Contractions, person, and the shapes models default to."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "too short to judge"
    per100 = 100 / len(w)
    contractions = len(COLLOQUIAL.findall(text)) * per100
    person = (len(PRONOUNS.findall(text)) + len(FORMAL_YOU.findall(text))) * per100
    tells = 0
    names = []
    for s in lex["structures"]:
        try:
            n = len(re.compile(s["regex"], re.MULTILINE).findall(text))
        except re.error:
            continue
        if n:
            tells += n
            names.append(s["id"])
    bullets = [len(b.split()) for b in re.findall(r"(?m)^\s*[-*•]\s+(.+)$", text)]
    uniform = (len(bullets) >= 3 and statistics.pstdev(bullets) < 1.6)
    score = (scale(contractions, human=4.0, machine=0.5) * 0.35
             + scale(person, human=8.0, machine=1.0) * 0.35
             + clamp(100 - tells * 22) * 0.30)
    if uniform:
        score -= 12
        names.append("uniform-bullets")
    detail = (f"{contractions:.1f} colloquial markers, {person:.1f} personal pronouns "
              f"per 100 words, {tells} structural tell(s)")
    if names:
        detail += " [" + ", ".join(names[:4]) + "]"
    return clamp(score), detail


CHECKS = ["BURSTINESS", "SPECIFICITY", "SLOP DENSITY", "FINGERPRINT", "VOICE"]


def run(text, lex):
    results = {}
    results["BURSTINESS"] = check_burstiness(text)
    results["SPECIFICITY"] = check_specificity(text)
    results["SLOP DENSITY"] = check_slop(text, lex)
    results["FINGERPRINT"] = check_fingerprint(text)
    results["VOICE"] = check_voice(text, lex)
    scores = [results[c][0] for c in CHECKS]
    # The weakest check drags the verdict: a detector only needs one signal.
    overall = statistics.mean(scores) * 0.6 + min(scores) * 0.4
    verdict = "PASS" if overall >= 70 and min(scores) >= 55 else (
        "REVIEW" if overall >= 50 else "FLAGGED")
    return results, overall, verdict


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render(results, overall, verdict, label=None, out=sys.stdout):
    title = "AI DETECTION PANEL (de)" + (f"  -  {label}" if label else "")
    print("\n" + title, file=out)
    print("=" * max(len(title), 62), file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {name:<13} {bar(score)} {score:5.1f}", file=out)
        print(f"  {'':<13} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'HUMAN SCORE':<13} {bar(overall)} {overall:5.1f}   {verdict}", file=out)
    if verdict != "PASS":
        weakest = min(CHECKS, key=lambda c: results[c][0])
        print(f"\n  Weakest signal: {weakest}. Fix that first.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Score how machine-written a draft looks.")
    ap.add_argument("input", nargs="?", default="-", help="file, or - for stdin")
    ap.add_argument("compare", nargs="?", help="second file, to show before/after")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lexicon", default=LEX)
    args = ap.parse_args()

    lex = json.load(open(args.lexicon, encoding="utf-8"))
    read = lambda p: sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()

    targets = [(args.input, read(args.input))]
    if args.compare:
        targets.append((args.compare, read(args.compare)))

    payload = []
    for name, text in targets:
        results, overall, verdict = run(text, lex)
        payload.append({
            "source": name,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "human_score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if args.compare else payload[0], indent=2, ensure_ascii=False))
        return

    for (name, text), p in zip(targets, payload):
        results, overall, verdict = run(text, lex)
        render(results, overall, verdict, label=os.path.basename(name) if args.compare else None)
    if args.compare:
        a, b = payload
        delta = b["human_score"] - a["human_score"]
        print(f"  {a['human_score']:.1f} {a['verdict']}  ->  "
              f"{b['human_score']:.1f} {b['verdict']}   ({delta:+.1f})\n")

    sys.exit(0 if payload[-1]["verdict"] == "PASS" else 1)


if __name__ == "__main__":
    main()
