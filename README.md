# LinkedIn agent skill - Deutsche Fassung

Elf Claude-Skills für einen deutschsprachigen LinkedIn-Auftritt. Deutsche
Adaption von [linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill)
von Jake Schincariol (MIT).

**Nichts wird gepostet, bevor du ja sagst.** Die Skills schreiben, du postest.

## Was an der deutschen Fassung anders ist

- Alle Anweisungen, Beispiele, 21 Hook-Formeln und die Profil-Rubrik auf Deutsch.
- **Du/Sie-Logik** in Posts, Kommentaren, Antworten und DMs (spiegeln, konservative
  Branchen siezen, nie mischen).
- Deutsche Zahlenformate (4.200 €, 30 %, 8:15 Uhr), deutsche Längen (Texte laufen
  rund ein Viertel länger), Postingzeiten für MEZ/MESZ inkl. Feiertage.
- Hinweis auf die Impressumspflicht bei geschäftlich genutzten Profilen.
- **Humanizer für Deutsch** (`li-human`):
  - eigenes Lexikon mit rund 150 deutschen KI-Floskeln und Lehnübersetzungen
    ("In der heutigen schnelllebigen Welt", "spielt eine entscheidende Rolle",
    "am Ende des Tages", "Gamechanger", "Lass das mal sacken")
  - Flexion: `nahtlos*` trifft nahtlose/nahtlosen und überträgt die Endung;
    Einträge mit `replace: null` werden nur markiert, weil Kasus und Satzstellung
    blindes Ersetzen im Deutschen oft falsch machen
  - Gedankenstrich wird zu ` - `, deutsche Anführungszeichen („“ ‚‘ »«) zu geraden
  - Satzerkennung ignoriert Abkürzungen (z. B., d. h., bzw.) und Ordinalzahlen (3. März)
  - SPECIFICITY zählt Zahlen, €, %, Akronyme und Marken statt großgeschriebener
    Wörter (im Deutschen ist jedes Substantiv groß)
  - VOICE zählt Umgangssprache und Modalpartikeln (gibt's, hab, halt, eben, mal,
    doch) statt englischer Kontraktionen
  - deutsche Strukturmuster: "Es geht nicht um X. Es geht um Y.", "nicht nur ...
    sondern auch", "Das Ergebnis?", "Was meint ihr?", Dreierlisten mit "und"

Skriptausgaben und Code-Kommentare bleiben englisch.

## Installation

**Claude Code, global:**

```bash
cp -r skills/li-* ~/.claude/skills/
mkdir -p ~/.claude/linkedin && cp templates/voice.md ~/.claude/linkedin/voice.md
```

**Claude Code, als Plugin aus einem lokalen Ordner oder eigenem Git-Repo:**

```
/plugin marketplace add <pfad-oder-github-user/repo>
/plugin install linkedin-agent-de
```

**claude.ai / Claude Desktop:** "Code-Ausführung und Dateierstellung" muss aktiv sein.
Dann Customize → Skills → "+" → "Create skill" → "Upload a skill" und jede
`li-*.zip` aus `claude-ai-upload/` einzeln hochladen, `li-human` zuerst (die anderen
rufen ihn auf). Hochgeladene Skills werden ab Claude Code v2.1.273 automatisch
auch in Claude Code synchronisiert (`/skills` zeigt sie unter "claude.ai sync").

Danach `templates/voice.md` ausfüllen (oder drei eigene Posts einfügen und
"schreib meine voice.md daraus" sagen).

## Die elf

| Befehl | Was er tut |
| --- | --- |
| `/li-post` | Eine Idee wird ein Post. Drei Hooks aus 21 Formeln, ein Entwurf, humanisiert. |
| `/li-comment` | Kommentare unter fremden Posts. Neun Typen. Nie "Toller Beitrag!". |
| `/li-reply` | Antworten unter eigenen Posts, sortiert nach Lead / Substanz / Peer / Support / Rauschen. |
| `/li-profile` | Profil-Score von 100 nach 12-Punkte-Rubrik, dann Neufassung. |
| `/li-plan` | Die Woche: was, wann, mit wem. |
| `/li-human` | Der deutsche Humanizer mit zwei lokalen Skripten. |
| `/li-carousel` | Dokument-Posts: Folientext, Cover, PDF. |
| `/li-repurpose` | Ein Video, Newsletter oder Transkript wird eine Woche Posts. |
| `/li-dm` | Einladungsnotiz (200 Zeichen), erste Nachricht, zwei Nachfassungen. |
| `/li-inbox` | Postfach sortieren, Sequenzen erkennen, Antworten entwerfen. |
| `/li-audit` | Post-mortem über veröffentlichte Posts nach Engagement-Rate. |

## Humanizer

```bash
python3 skills/li-human/humanize.py entwurf.txt -o sauber.txt --report
python3 skills/li-human/detect.py entwurf.txt sauber.txt
```

Unter Windows `python` statt `python3`. Keine Abhängigkeiten, läuft lokal. Die fünf Checks sind lokale Heuristiken,
nicht GPTZero, Originality & Co., und versprechen deren Urteil nicht.

## Das Kleingedruckte

Die Skills posten nicht auf LinkedIn und sollen es nicht: automatisiertes Posten
oder Scraping verstößt gegen die
[LinkedIn-Nutzervereinbarung](https://www.linkedin.com/legal/user-agreement).
Nichts wird erfunden: fehlt eine Zahl, steht `{{deine Zahl}}` im Entwurf.

## Lizenz

MIT. Original © Jake Schincariol ([opusjake.ai](https://opusjake.ai)), deutsche Adaption ebenfalls MIT.
