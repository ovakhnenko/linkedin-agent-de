---
name: li-inbox
description: "Sortiert LinkedIn-Nachrichten in Lead/Recruiter/Peer/Bitte/Spam, erkennt Sequenzen, entwirft deutsche Antworten. Bei 'sortier mein Postfach', 'soll ich antworten'."
---

# li-inbox

Die meisten LinkedIn-Postfächer sind zu 80 % Rauschen, und der Preis dafür ist,
dass die anderen 20 % eine Woche liegen bleiben. Dieser Skill trennt beides und
schreibt nur, was sich lohnt.

## Input

Der Nutzer fügt die Nachrichten ein. Screenshots sind ok. Nicht in sein Konto
einloggen und das Postfach nicht per Browser lesen.

## Fünf Eimer

| Eimer | Signal | Aktion |
| --- | --- | --- |
| **LEAD** | beschreibt ein Problem, das der Nutzer löst, oder fragt nach Zusammenarbeit | heute antworten, vollständig |
| **RECRUITER** | eine Stelle, eine Firma, ein Gehaltsrahmen | antworten, wenn die Stelle echt ist, sonst eine Zeile |
| **PEER** | jemand aus dem Feld mit etwas zu sagen | diese Woche, menschlich |
| **BITTE** | will Rat, Zeit, eine Vorstellung, einen Gefallen | antworten, wenn es billig und konkret ist, sonst sauber absagen |
| **SPAM** | Agentur-Pitch, Lead-Gen-Sequenz, Krypto, "kurze Frage" ohne Frage | archivieren, keine Antwort |

Zuerst die Zahlen. "3 Leads, 2 Recruiter, 41 Spam" ist schon der halbe Wert.

## Eine Sequenz erkennen

Automatisierte Ansprache hat eine Form: Einladung ohne Bezug, Nachricht
Minuten nach der Annahme, "kurze Frage", "Ich habe gesehen, dass Sie in der
{Branche} tätig sind", Kalenderlink in Nachricht eins, "ich wollte nur kurz
nachhaken" exakt vier Tage später, oft ein Du/Sie-Wechsel zwischen Vorlagen.
Dann SPAM, und sag, welches Merkmal es verraten hat.

## Antworten

- **LEAD**: die Frage in der Nachricht vollständig und kostenlos beantworten.
  Passt es, ist das Angebot ein Satz am Ende. Passt es nicht, sag das und
  verweise auf etwas Hilfreiches.
- **RECRUITER**: ist die Stelle interessant, nach den drei Dingen fragen, die
  fehlen: Gehaltsrahmen (brutto/Jahr), Ebene, Remote/Hybrid/Büro. Sonst eine
  Zeile: suche nicht, empfehle gern weiter, und das ernst meinen.
- **BITTE**: unter zehn Minuten und konkret: machen. "Kann ich dich mal kurz
  anzapfen?": in einem freundlichen Satz absagen und die eine Antwort geben,
  die du im Call gegeben hättest.
- **ABSAGEN** sind kurz, freundlich, endgültig. Kein "Lass uns im Q3 nochmal
  sprechen", wenn es kein Q3 gibt.
- **Anrede** der eingehenden Nachricht übernehmen.

## Output

Nach Eimern gruppiert, Zahlen zuerst, Entwürfe nur für die Eimer mit Antwort,
jeder humanisiert. Dann die Schranke: der Nutzer verschickt.

```
POSTFACH  ·  52 Einträge  ·  3 LEAD, 2 RECRUITER, 4 PEER, 2 BITTE, 41 SPAM

SPAM  (41) - archivieren. 38 sind dieselbe Sequenz: Einladung ohne Bezug,
"kurze Frage" 4 Minuten nach Annahme, Kalenderlink in Nachricht eins.
```
