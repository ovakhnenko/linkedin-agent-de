---
name: li-human
description: "Entfernt KI-Floskeln, Gedankenstriche und unsichtbare Zeichen aus deutschen Texten und bewertet sie (5 Checks). Bei 'humanisieren', 'klingt das nach KI', vor jedem LinkedIn-Text."
---

# li-human

Zwei Werkzeuge liegen in diesem Ordner, und beide laufen wirklich. Benutze sie.
Nicht nach Augenmaß.

```bash
python3 humanize.py entwurf.txt -o sauber.txt --report   # säubern, Änderungen zeigen
python3 detect.py entwurf.txt                             # bewerten, fünf Checks
python3 detect.py entwurf.txt sauber.txt                  # Vorher/Nachher belegen
```

Beide lesen `slop.json`, das deutsche Lexikon: rund 150 Floskeln, Wörter und
Lehnübersetzungen, 17 unsichtbare Zeichenklassen, Typografie-Ersetzungen und
13 Strukturmuster. Die Datei soll bearbeitet werden: Benutzt der Nutzer ein
Wort, das das Lexikon entfernt, nimm es raus.

## Lexikon-Regeln (wichtig für Deutsch)

- `"stamm*"` trifft alle Flexionsformen und überträgt die Endung:
  nahtlose -> reibungslose, innovativen -> neuen. Bei Adjektiven nur echte
  Endungen, "Robustheit" bleibt also unberührt.
- `"replace": null` heißt **nur markieren**. Deutsche Satzstellung, Kasus und
  Genus machen blindes Ersetzen oft falsch ("eine Vielzahl von Vorteilen" ->
  "viele Vorteile", nicht "viele Vorteilen"). Diese Treffer formulierst du
  selbst um.
- Ersatz-Substantive müssen das Genus behalten (der Mehrwert -> der Nutzen).
  Wer neue Einträge ergänzt, prüft das.

## Was automatisch korrigiert wird

**1. Unsichtbare Zeichen.** Nullbreite Leerzeichen und Verbinder, Wortverbinder,
weiche Trennstriche, BOMs, Unicode-Tag-Zeichen, geschützte und schmale
Leerzeichen. Eine Tastatur erzeugt sie nicht, sie überleben Copy-Paste.

**2. Typografie.** Geviertstrich und Gedankenstrich (` – `) werden zu ` - `,
weil das ist, was Menschen tippen. „Deutsche“ und “englische” Anführungszeichen
sowie »Guillemets« werden zu geraden, Auslassungspunkte zu drei Punkten,
Aufzählungspunkte zu Bindestrichen.

**3. Das Floskel-Lexikon.** "In der heutigen schnelllebigen Welt", "darüber
hinaus", "letztendlich", "spielt eine entscheidende Rolle", "Lass das mal
sacken", "Gamechanger" usw., jeweils durch ein schlichtes Wort ersetzt oder
gelöscht, Großschreibung erhalten, URLs unangetastet.

## Was NICHT automatisch korrigiert wird

Strukturmuster werden **markiert, nicht umgeschrieben**:

- "Es geht nicht um X. Es geht um Y." und "nicht nur X, sondern auch Y"
- "Das ist nicht X, sondern Y"
- Dreierlisten: "Unternehmen, Mitarbeitende und Kunden."
- Rhetorische Einwort-Fragen: "Das Ergebnis?"
- Inszenierte Enthüllungen: "Die Wahrheit:", "Meine Learnings:"
- Raketen-, Feuer-, Glühbirnen-, Funkel-, Ziel-, Zeigefinger- und Haken-Emoji
- Hashtag-Wände, doppelte Ausrufezeichen
- Reflex-Köder: "Was meint ihr?", "Wer kennt's?", "Seht ihr das auch so?"
- Gleichförmige Satz- und Aufzählungslängen
- alle `null`-Treffer aus dem Lexikon (Abschnitt 4 im Report)

Das ist deine Arbeit. Jede markierte Zeile von Hand umschreiben, Bedeutung
behalten, dann `detect.py` erneut laufen lassen. Genau das bringt den Score von
REVIEW auf PASS.

## Die fünf Checks

`detect.py` bewertet fünf Signale von 0-100, höher ist menschlicher:

| Check | misst | Maschine sieht so aus |
| --- | --- | --- |
| BURSTINESS | Variation der Satzlänge (Abkürzungen wie "z. B." zählen nicht als Satzende) | jeder Satz gleich lang |
| SPECIFICITY | Zahlen, €, %, Akronyme (SAP, KMU), Marken (LinkedIn, PowerShell), Wochentage, @Erwähnungen pro 100 Wörter | abstrakte Substantive, keine Zahlen |
| SLOP DENSITY | Lexikon-Treffer pro 100 Wörter | Floskel-Vokabular |
| FINGERPRINT | unsichtbare Zeichen, Geviertstriche, typografische Anführungszeichen pro 1.000 Zeichen | typografisch perfekt |
| VOICE | Umgangssprache (gibt's, hab, 'ne, halt, eben, mal, ja, doch), Pronomen (ich, wir, du, ihr), Strukturmuster | keine Modalpartikeln, inszenierte Enthüllungen |

Hinweis: Großgeschriebene Wörter zählen im Deutschen nicht als Namen, weil
jedes Substantiv groß geschrieben wird. Modalpartikeln sind das stärkste
deutsche Signal für einen Menschen; Modelle lassen sie fast immer weg.

Das Urteil gewichtet den Mittelwert mit 60 % und den **schwächsten einzelnen
Check** mit 40 %, weil ein Detektor nur ein Signal braucht. PASS braucht
insgesamt 70+ und keinen Check unter 55.

## Ehrlich bleiben

Das sind fünf lokale Heuristiken, modelliert nach den Signalen, auf die
öffentliche Detektoren achten. Sie laufen komplett lokal, nichts wird
hochgeladen. Sie sind **nicht** GPTZero, Originality, Copyleaks, Winston oder
Turnitin, rufen deren APIs nicht auf und können deren Urteil nicht versprechen.
Sag einem Nutzer nie, sein Text sei "unerkennbar".

## Reihenfolge

1. `python3 humanize.py entwurf.txt -o sauber.txt --report`
2. Abschnitte 4 und 5 des Reports lesen. Diese Stellen selbst umschreiben.
3. `python3 detect.py entwurf.txt sauber.txt` für Vorher/Nachher.
4. Kein PASS? Den im Output genannten schwächsten Check beheben, nochmal.
   Zwei Runden sind normal. Fünf heißen: der Entwurf ist nach Schema
   geschrieben, die Lösung ist ein neuer Entwurf, nicht mehr Durchläufe.
5. Dem Nutzer den sauberen Text und den Score zeigen. Nie nur den Score.
