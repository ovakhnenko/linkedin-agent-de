---
name: li-audit
description: "Post-mortem über veröffentlichte LinkedIn-Posts nach Engagement-Rate und Reichweiten-Faktor. Bei 'was funktioniert', 'warum gefloppt', 'analysier meine Statistiken'."
---

# li-audit

Die einzige ehrliche Quelle dafür, was bei einem Konto funktioniert, ist dieses
Konto. Jede Regel in jedem LinkedIn-Ratgeber, auch in diesem Paket, ist eine
Annahme. Die letzten 30 Posts des Nutzers sind der Beweis.

## Input

Was der Nutzer hat:

- Den Export der Beitragsanalysen aus LinkedIn (Analysen, Inhalte,
  Exportieren). CSV oder XLSX. Spaltennamen können deutsch sein
  (Impressionen, Reaktionen, Kommentare, Reposts); ordne sie zu.
- Oder einen Screenshot pro Post mit Impressionen, Reaktionen, Kommentaren, Reposts.
- Oder nur die Posts mit Reaktionszahlen, für einen ersten Durchgang reicht das.

Lies auch `~/.claude/linkedin/log.md`, falls vorhanden: dort steht, welche
Hook-Formel jeder Post benutzt hat.

## Was wirklich messen

Reine Impressionen sind die unwichtigste Zahl, weil sie vor allem davon
abhängen, wie viele schon folgen. Stattdessen, mit Rechenweg:

| Kennzahl | Berechnung | sagt aus |
| --- | --- | --- |
| **Engagement-Rate** | (Reaktionen + Kommentare + Reposts) / Impressionen | ob der Post seine Reichweite verdient hat |
| **Kommentar-Quote** | Kommentare / Reaktionen | ob er etwas ausgelöst oder nur ein Nicken bekommen hat |
| **Reichweiten-Faktor** | Impressionen / Follower | ob er über das bestehende Publikum hinauskam |
| **Speichern/Senden** | falls vorhanden | der stärkste Einzelindikator für künftige Reichweite |

Nach Engagement-Rate und Reichweiten-Faktor ranken, nicht nach Impressionen.
900 Impressionen mit 40 Kommentaren schlagen 12.000 mit 6.

## Dann das Muster finden

Top 5 und Flop 5 nebeneinander, suchen, was sie wirklich trennt, und bereit
sein, etwas zu schließen, das der Nutzer nicht hören will:

- Hook-Formel. Welche Nummern aus `hooks.json` sind in den Top 5?
- Format. Text, Dokument, Bild, Video.
- Länge.
- Thema.
- Anrede (Du/Sie) und Sprache (Deutsch/Englisch), falls gemischt.
- Wochentag und Uhrzeit, **zuletzt**, und nur wenn sonst nichts auffällt.
- Kommentare in der ersten Stunde: hat der Nutzer innerhalb einer Stunde geantwortet?

Den Befund als Aussage mit Beleg und Sicherheit formulieren. Mit 30 Posts sieht
man ein Muster, mit 6 nicht, und das sagst du dann, statt eins zu erfinden.

## Output

```
AUDIT  ·  31 Posts  ·  12.06. - 05.09.

TOP 5 NACH ENGAGEMENT-RATE
  8,1 %  #3  Fehler      "18.000 € hat mich ein fehlender Vertrag gekostet"   1.940 Impr.
  6,4 %  #20 Abschied    "Ich habe meinen bestzahlenden Kunden gekündigt"     2.210 Impr.
  ...

FLOP 5
  0,4 %  #5  Liste       "7 Tools, die jeder Gründer braucht"                11.400 Impr.
  ...

WAS DIE DATEN SAGEN
1. Posts, in denen du schlecht aussiehst: Schnitt 6,2 % gegen 1,1 % beim Rest.
   n=6. Dein stärkstes Signal, mit Abstand.
2. Tool-Listen bringen Impressionen und sonst nichts. Hohe Reichweite, keine
   Kommentare, keine Leads. Drei deiner Flop 5.
3. Der Wochentag zeigt nichts. Dienstag und Freitag liegen im Rauschen.
   Hör auf, das zu optimieren.

STOPP: Tool-Listen.
MEHR: die mit einem Preis, den du gezahlt hast, und einer Zahl.
```

Dann die Schlüsse an `/li-plan` übergeben, damit der nächste Wochenplan auf den
eigenen Daten des Nutzers steht.
