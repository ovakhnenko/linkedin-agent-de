---
name: li-repurpose
description: "Macht aus Video, Podcast, Newsletter oder Transkript eine Woche deutscher LinkedIn-Posts. Bei 'mach daraus Posts', 'verwerte das weiter'."
---

# li-repurpose

Ein guter langer Inhalt enthält vier bis sechs Posts. Die meisten holen einen
raus und werfen den Rest weg.

## Input

Transkript, Artikel, Newsletter, Skript, Gesprächsnotiz. Bei einer YouTube-URL:
ein Transkript-Tool nutzen, falls in der Sitzung vorhanden, sonst um den Text
bitten. Alles lesen, bevor du etwas herausziehst.

Ist die Quelle englisch: nicht übersetzen, sondern auf Deutsch neu schreiben.
Englische Redewendungen ("move the needle", "at the end of the day") werden
nicht wörtlich übernommen, das sind genau die Lehnübersetzungen, die
`/li-human` markiert. Dollarbeträge nur umrechnen, wenn der Nutzer das will;
sonst als Dollar stehen lassen und kennzeichnen.

## Herausziehen, nicht zusammenfassen

Eine Zusammenfassung ist kein Post. Zieh heraus, was allein steht:

| Fund | was es ist |
| --- | --- |
| **Thesen** | jeder Satz, der eine Diskussion auslösen würde |
| **Zahlen** | jede Zahl, jeder Betrag, jede Dauer, jeder Prozentwert |
| **Geschichten** | jeder Moment mit einer Person, einer Szene und einem Preis |
| **Mechanismen** | jede "so funktioniert das"-Erklärung |
| **Fehler** | jedes Eingeständnis, dass etwas schiefging |
| **Sätze** | jeder Satz, der schon so zitierfähig ist |

Erst die Funde mit Anzahl auflisten, dann schreiben. Weniger als vier Funde:
die Quelle ist dünn, und vier Posts daraus werden auch dünn. Sag das.

## Dann die Woche bauen

Jeder Fund wird ein Post, und jeder Post steht komplett für sich. Der Leser hat
das Video nicht gesehen und wird es nie sehen. Nie "wie in meinem letzten
Video erwähnt".

Jedem eine Hook-Formel aus `li-post/hooks.json` zuweisen, und variieren: fünf
Posts aus einer Quelle mit gleicher Hook-Form wirken wie eine Content-Fabrik.

Reihenfolge: stärkste These zuerst, Geschichte in der Wochenmitte, Mechanismus
zuletzt.

## Output

```
QUELLE: "Warum wir das Erstgespräch abgeschafft haben" (18 Min., 3.400 Wörter)

FUNDE  4 Thesen, 6 Zahlen, 2 Geschichten, 3 Mechanismen, 1 Fehler, 5 zitierfähige Sätze

WOCHE
DI  #1  Gegenthese     Das Erstgespräch ist eine Steuer auf eine schlechte Website
MI  #17 Zeitanker      6 Stunden pro Woche zurück, weil wir einen Kalenderlink gelöscht haben
DO  #9  Kaltstart      "Können wir nicht kurz telefonieren?"
FR  #21 Direkter Wert  Das 4-Fragen-Formular, das den Call ersetzt. Zum Mitnehmen.

Sag "schreib Dienstag" und ich entwerfe ihn.
```

Dann auf Zuruf einzeln entwerfen, jeweils über `/li-post` und `/li-human`.
Nicht vier fertige Posts auf einmal: die klingen alle gleich, und der Nutzer
bearbeitet keinen davon.
