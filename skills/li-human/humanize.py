#!/usr/bin/env python3
"""
humanize.py - strip the machine fingerprint out of a German draft.

German edition of the li-human humanizer. Three passes, in this order:

  1. INVISIBLE   delete or normalise the characters a human keyboard never
                 produces: zero-width joiners, word joiners, soft hyphens,
                 BOMs, Unicode tag characters, non-breaking and narrow spaces.
  2. TYPOGRAPHIC em dash and spaced en dash (Gedankenstrich) -> " - ",
                 curly and German quotes („“ ‚‘ »«) -> straight,
                 ellipsis -> three dots, bullet -> hyphen.
  3. LEXICAL     replace the German slop lexicon in slop.json with plain words,
                 preserving capitalisation and leaving URLs untouched.

Lexicon conventions:
  "stem*"          matches any inflection; "repl*" carries the suffix over
                   (nahtlose -> reibungslose).
  replace ""       delete the match.
  replace null     FLAG ONLY - reported, never replaced. German verb position
                   and inflection make blind replacement wrong too often.

Structural tells are REPORTED, never auto-rewritten.

Usage
  python3 humanize.py draft.txt
  python3 humanize.py draft.txt --report
  python3 humanize.py draft.txt -o clean.txt --report
  python3 humanize.py draft.txt --json
"""

import argparse
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop.json")

URL_RE = re.compile(r"https?://\S+|www\.\S+|\S+@\S+\.\S+")
SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")

# German abbreviations and ordinals whose dot is not a sentence end.
ABBR_RE = re.compile(
    r"\b(?:z\.\s?B|d\.\s?h|u\.\s?a|o\.\s?ä|u\.\s?U|s\.\s?o|s\.\s?u|i\.\s?d\.\s?R|"
    r"bzw|ca|ggf|usw|etc|Nr|Dr|Prof|inkl|exkl|evtl|vgl|zzgl|bspw|sog|max|min|"
    r"Mio|Mrd|Tsd|Std|Min|Jh|Abs|Str|Tel)\.",
    re.IGNORECASE)
ORDINAL_RE = re.compile(
    r"(\d)\.(?=\s+(?:[a-zäöüß]|Januar|Februar|März|April|Mai|Juni|Juli|August|"
    r"September|Oktober|November|Dezember|Jan|Feb|Mär|Apr|Jun|Jul|Aug|Sep|Okt|Nov|Dez)\b)")
MASK = "⁣"  # invisible separator, only used internally and removed again


def mask_abbr(text):
    text = ABBR_RE.sub(lambda m: m.group(0).replace(".", MASK), text)
    return ORDINAL_RE.sub(lambda m: m.group(1) + MASK, text)


def sentence_lengths(text):
    return [len(s.split()) for s in SENT_RE.findall(mask_abbr(text)) if len(s.split()) > 2]


def utf8_stdio():
    """Windows consoles and pipes default to cp125x, which cannot encode ä/ö/ü for all locales."""
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def read_text(path):
    """Read a file or stdin ("-"). UTF-8 (with or without BOM) first, cp1252 as fallback."""
    if path == "-":
        return sys.stdin.read()
    with open(path, "rb") as fh:
        data = fh.read()
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return data.decode("cp1252", errors="replace")


def load_lexicon(path=LEX):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _cp(spec):
    if "-" in spec:
        a, b = spec.split("-")
        return (int(a[2:], 16), int(b[2:], 16))
    return int(spec[2:], 16)


def protect_urls(text):
    found = []

    def stash(m):
        found.append(m.group(0))
        return f"\x00URL{len(found) - 1}\x00"

    return URL_RE.sub(stash, text), found


def restore_urls(text, found):
    for i, url in enumerate(found):
        text = text.replace(f"\x00URL{i}\x00", url)
    return text


ADJ_SUFFIX = r"(?:e[mnrs]?|er(?:e[mnrs]?)?|st(?:e[mnrs]?)?)?"


def lex_pattern(find, family=""):
    """Compile a lexicon entry. Word boundaries only where the edge is a word char."""
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


def pass_invisible(text, lex):
    hits = []
    for entry in lex["invisible"]:
        cp = _cp(entry["cp"])
        if isinstance(cp, tuple):
            pattern = "[" + re.escape(chr(cp[0])) + "-" + re.escape(chr(cp[1])) + "]"
        else:
            pattern = re.escape(chr(cp))
        n = len(re.findall(pattern, text))
        if n:
            hits.append({"name": entry["cp"] + " " + entry["name"], "count": n,
                         "action": entry["action"]})
            text = re.sub(pattern, "" if entry["action"] == "delete" else " ", text)
    stray = [c for c in text if unicodedata.category(c) == "Cf"]
    if stray:
        hits.append({"name": "other invisible format chars", "count": len(stray),
                     "action": "delete"})
        text = "".join(c for c in text if unicodedata.category(c) != "Cf")
    return text, hits


def pass_typographic(text, lex):
    hits = []
    for entry in lex["typographic"]:
        ch = entry["from"]
        n = text.count(ch)
        if not n:
            continue
        hits.append({"name": f"{ch} {entry['name']}", "count": n,
                     "to": entry["to"].strip() or "(space)"})
        if ch == "—":
            # German uses the dash as Gedankenstrich; a spaced hyphen is what people type.
            text = re.sub(r"[ \t]*—[ \t]*", " - ", text)
        elif ch == "–":
            text = re.sub(r"(?<=\d)[ \t]*–[ \t]*(?=\d)", "-", text)   # 5–10 -> 5-10
            text = re.sub(r"[ \t]*–[ \t]*", " - ", text)                # Gedankenstrich
        elif ch == "·":
            # Gender point inside a word (Kund·innen) is deliberate; only free-standing dots go.
            n = len(re.findall(r"(?<!\w)·|·(?!\w)", text))
            if not n:
                hits.pop()
                continue
            hits[-1]["count"] = n
            text = re.sub(r"(?<!\w)·|·(?!\w)", entry["to"], text)
        else:
            text = text.replace(ch, entry["to"])
    text = re.sub(r"(?m)^ - ", "- ", text)          # dash at line start = bullet
    text = re.sub(r" - (?=[,.;:!?])", "", text)     # dangling dash before punctuation
    return text, hits


def _match_case(src, repl):
    if not repl:
        return repl
    if src.isupper() and len(src) > 1:
        return repl.upper()
    if src[0].isupper():
        return repl[0].upper() + repl[1:]
    return repl


LINE_START = "\x01"


def pass_lexical(text, lex):
    """Replace or flag slop words and phrases. Longest first so phrases win."""
    hits, flags = [], []
    entries = sorted(lex["phrases"] + lex["words"],
                     key=lambda e: len(e["find"].rstrip("*")), reverse=True)
    for entry in entries:
        find, repl = entry["find"], entry["replace"]
        pattern = lex_pattern(find, entry["family"])
        found = [m.group(0) for m in pattern.finditer(text)]
        if not found:
            continue
        if repl is None:
            flags.append({"find": find, "count": len(found), "family": entry["family"],
                          "examples": sorted(set(found))[:3]})
            continue
        hits.append({"find": find, "replace": repl or "(deleted)",
                     "count": len(found), "family": entry["family"]})

        def sub(m, repl=repl, find=find):
            if find.endswith("*"):
                new = _match_case(m.group(1), repl.rstrip("*")) + m.group(2)
            else:
                new = _match_case(m.group(1), repl)
            if not new:
                before = text[:m.start()].rstrip(" \t")
                # Line start or sentence end: the next word has to be capitalised.
                at_start = before == "" or before[-1] in "\n.!?"
                return LINE_START if at_start else ""
            return new

        text = pattern.sub(sub, text)
    # Clean up after deletions.
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r",[ \t]*,", "", text)             # "Wir sind, <deleted>, fertig"
    text = re.sub(LINE_START + r"[ \t,;:]*([a-zäöü])", lambda m: m.group(1).upper(), text)
    text = text.replace(LINE_START, "")
    text = re.sub(r"(?m)^[ \t]*([,.;:])\s*", "", text)
    text = re.sub(r"[ \t]+([,.;:!?])", r"\1", text)
    text = re.sub(r"(?m)^[ \t]+|[ \t]+$", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text, hits, flags


def scan_structures(text, lex):
    flags = []
    for s in lex["structures"]:
        try:
            pattern = re.compile(s["regex"], re.MULTILINE)
        except re.error:
            continue
        found = pattern.findall(text)
        if found:
            flags.append({"name": s["name"], "count": len(found), "fix": s["fix"]})
    lens = sentence_lengths(text)
    if len(lens) >= 4:
        mean = sum(lens) / len(lens)
        var = sum((n - mean) ** 2 for n in lens) / len(lens)
        cv = (var ** 0.5) / mean if mean else 0
        if cv < 0.35:
            flags.append({
                "name": f"Uniform sentence length (variation {cv:.2f})",
                "count": len(lens),
                "fix": "Break one sentence in half. Let another run long. Machines write even.",
            })
    return flags


def humanize(text, lex):
    text, urls = protect_urls(text)
    text, inv = pass_invisible(text, lex)
    text, typo = pass_typographic(text, lex)
    text, lexi, lexflags = pass_lexical(text, lex)
    text = restore_urls(text, urls)
    return text.strip() + "\n", {
        "invisible": inv,
        "typographic": typo,
        "lexical": lexi,
        "lexical_flags": lexflags,
        "structures": scan_structures(text, lex),
    }


def render_report(report, out=sys.stderr):
    def head(title):
        print(f"\n{title}\n" + "-" * len(title), file=out)

    total = sum(h["count"] for h in report["invisible"]) \
        + sum(h["count"] for h in report["typographic"]) \
        + sum(h["count"] for h in report["lexical"])
    flagged = len(report["structures"]) + len(report["lexical_flags"])

    head("HUMANIZE REPORT (de)")
    print(f"{total} machine artefacts removed, {flagged} items flagged for manual rewrite",
          file=out)

    if report["invisible"]:
        head("1. INVISIBLE CHARACTERS")
        for h in report["invisible"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['action']}", file=out)
    if report["typographic"]:
        head("2. TYPOGRAPHY")
        for h in report["typographic"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['to']}", file=out)
    if report["lexical"]:
        head("3. SLOP LEXICON (replaced)")
        for h in report["lexical"]:
            print(f"  {h['count']:>3}x  {h['find']}  -> {h['replace']}   [{h['family']}]", file=out)
    if report["lexical_flags"]:
        head("4. SLOP LEXICON (flagged only - rephrase by hand, German grammar)")
        for h in report["lexical_flags"]:
            ex = ", ".join(h["examples"])
            print(f"  {h['count']:>3}x  {h['find']}   [{h['family']}]  e.g. {ex}", file=out)
    if report["structures"]:
        head("5. STRUCTURAL TELLS  (not auto-fixed - rewrite these yourself)")
        for h in report["structures"]:
            print(f"  {h['count']:>3}x  {h['name']}\n        {h['fix']}", file=out)
    if not any(report.values()):
        head("CLEAN")
        print("  Nothing to strip.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Strip the machine fingerprint out of a German draft.")
    ap.add_argument("input", nargs="?", default="-", help="file, or - for stdin")
    ap.add_argument("-o", "--out", help="write cleaned text here instead of stdout")
    ap.add_argument("--report", action="store_true", help="print what changed, to stderr")
    ap.add_argument("--json", action="store_true", help="emit {text, report} as JSON")
    ap.add_argument("--lexicon", default=LEX, help="path to slop.json")
    args = ap.parse_args()

    utf8_stdio()
    try:
        raw = read_text(args.input)
    except OSError as e:
        ap.error(f"cannot read {args.input}: {e.strerror}")
    lex = load_lexicon(args.lexicon)
    clean, report = humanize(raw, lex)

    if args.json:
        print(json.dumps({"text": clean, "report": report}, indent=2, ensure_ascii=False))
        return
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(clean)
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(clean)
    if args.report:
        render_report(report)


if __name__ == "__main__":
    main()
