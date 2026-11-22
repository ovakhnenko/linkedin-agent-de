---
name: li-plan
description: "Plant die LinkedIn-Woche für DACH: was, wann (MEZ), mit wem interagieren. Bei 'plan meine Woche', 'was soll ich posten', 'Redaktionsplan'."
---

# li-plan

Die Leitstelle. Alles andere im Paket führt aus, das hier entscheidet, was
ausgeführt wird. Einmal pro Woche, immer am selben Tag.

## Input

Existieren `~/.claude/linkedin/voice.md` und `log.md`, lies sie: der Plan soll
kein Thema der letzten zwei Wochen wiederholen. Sonst nach vier Dingen fragen
und sie notieren:

1. Was der Nutzer verkauft, und an wen.
2. Die drei oder vier Themen, für die er bekannt sein will.
3. Was diese Woche wirklich passiert ist: ein Kundengespräch, eine Zahl, ein
   Fehler, etwas Gebautes, eine Diskussion. Daraus entstehen Posts.
4. Zehn bis zwanzig Personen oder Firmen, bei denen er sichtbar sein will.

## Was posten

Vier Posts pro Woche schlagen sieben. Der fünfte Post einer Woche ist fast
immer der schwache, der den Schnitt runterzieht.

Über die Woche mischen, nie zwei vom gleichen Typ hintereinander:

| Typ | Anteil | Aufgabe |
| --- | --- | --- |
| **Beleg** | 1 pro Woche | etwas, das passiert ist, mit Zahl |
| **Meinung** | 1 pro Woche | eine Position, die Follower kosten könnte |
| **Wissen** | 1 pro Woche | eine Sache, die der Leser heute umsetzen kann |
| **Geschichte** | 1 alle zwei Wochen | eine Szene mit Dialog und einem Preis |
| **Angebot** | 1 alle zwei Wochen | was du verkaufst, klar gesagt, ohne Entschuldigung |

Für jeden Slot: Thema, der konkrete Winkel aus dieser Woche, und die
Hook-Nummer aus `li-post/hooks.json`. Kein Thema, ein Winkel. "KI" ist kein
Plan. "Das Angebot, das wir verloren haben, weil im KI-Entwurf ein
Gedankenstrich stand" ist ein Post.

## Wann posten

Wenn das Publikum am Schreibtisch sitzt. Für B2B im DACH-Raum (MEZ/MESZ) ist
der Standard: **Dienstag bis Donnerstag, 7:30-9:00 Uhr**, zweite Wahl die
Mittagspause 12:00-13:00 Uhr sowie Montagnachmittag und Freitagvormittag.
Feiertage (bundeslandabhängig, z. B. Fronleichnam in BW/BY) und Brückentage
meiden, im August mit Urlaubsflaute rechnen. Wochenende nur für persönliche
Geschichten, oder gar nichts.

Aber klar sagen: **Tag und Uhrzeit zählen viel weniger als die erste Zeile.**
Wer Zeiten optimiert, bevor die Hooks funktionieren, poliert das Falsche.

Zeiten auf die Zeitzone des Publikums beziehen, nicht des Nutzers.

## Mit wem interagieren

Liste mit 10, dreigeteilt:

- **5 Reichweite**: Leute mit dem Publikum, das der Nutzer will, deren Posts er
  wirklich ergänzen kann. Kommentieren, bevor 20 Kommentare drunter stehen.
- **3 Peers**: gleiche Ebene, gleiches Feld. Diese Gruppe erwidert.
- **2 Käufer**: Leute, die wirklich kaufen könnten. Wochenlang kommentieren,
  bevor eine DM kommt, und nie im Kommentar pitchen.

20 Minuten am Tag, vor dem Posten, nicht danach.

## Output

```
WOCHE AB 07.09.

MO  nur Engagement  (20 Min., Liste unten)
DI  8:15 Uhr  BELEG       #17 Zeitanker      - Angebot von 5 Std. auf 20 Min.
MI  nur Engagement
DO  8:00 Uhr  MEINUNG     #1  Gegenthese     - warum wir das Erstgespräch abgeschafft haben
FR  8:30 Uhr  WISSEN      #21 Direkter Wert  - die 4-Zeilen-Mail zum Wiederbeleben, verschenkt
SA  -
SO  17:00 Uhr GESCHICHTE  #9  Kaltstart      - die "wir nehmen jemand Günstigeren"-Mail

ENGAGEMENT  (5 Reichweite / 3 Peers / 2 Käufer)
  ...

Sag "schreib Dienstag" und ich entwerfe ihn.
```

Den Plan in `~/.claude/linkedin/plan.md` schreiben, damit die anderen Skills
ihn lesen können. Nichts wird irgendwo geplant oder gepostet.
