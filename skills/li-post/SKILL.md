---
name: li-post
description: "Schreibt deutsche LinkedIn-Posts aus einer Idee: 3 Hooks aus 21 Formeln, ein Entwurf, humanisiert. Bei 'schreib einen LinkedIn-Post', 'Hook', 'Beitrag über X'."
---

# li-post

Macht aus einer rohen Idee einen deutschen LinkedIn-Beitrag, der klingt wie die
Person, die ihn postet.

## Bevor du schreibst

1. Lies `~/.claude/linkedin/voice.md`, falls vorhanden. Das ist das
   Stimmprofil: wie der Nutzer spricht, was er nie sagt, **Du oder Sie**, ob und
   wie er gendert, wie viel Englisch erlaubt ist. Fehlt die Datei, bitte um
   **drei eigene frühere Beiträge**, leite die Stimme daraus ab und schreib die
   Datei. Erfinde keine Stimme. Ein Post in der falschen Stimme ist schlechter
   als kein Post.
2. Lies `hooks.json` in diesem Ordner: 21 Formeln mit Vorlage, Beispiel, Zweck
   und dem typischen Fehler.
3. Ist die Idee dünn ("Post über KI"), nicht aufblasen. Stell eine gebündelte
   Frage: Was ist passiert, wem, und was hat es gekostet oder gebracht? Ein Post
   braucht eine konkrete, wahre Sache.

## Die Form

LinkedIn belohnt Verweildauer, Speichern und Kommentare, in dieser Reihenfolge.

```
Zeile 1   der Hook. Allein. Muss die Kürzung bei ~140 Zeichen (mobil) überleben.
          Deutsche Wörter sind lang: der Hook ist eher 8 als 14 Wörter.
Zeile 2   die Auflösung von Zeile 1, keine Einleitung für Zeile 3.
Körper    kurze Absätze, 1-3 Zeilen, Leerzeile zwischen jedem. Keine Textwand.
Die Wende eine Zeile, die das Vorherige neu einordnet.
Schluss   eine konkrete Frage ODER eine Aufforderung. Nie beides.
```

Länge: 1.000-1.600 Zeichen für einen Textbeitrag (Deutsch läuft rund ein
Viertel länger als Englisch). Unter 450 wirkt wie ein Gedanke, über 2.200 muss
sich jede Zeile verdienen. LinkedIn erlaubt maximal 3.000.

## Deutsche Regeln

- **Anrede** aus voice.md. Ohne Angabe: Du im Feed (auf LinkedIn im DACH-Raum
  üblich), aber nie gemischt innerhalb eines Posts.
- **Zahlen deutsch:** 4.200 €, 30 %, 8:15 Uhr, 12.03. Keine Dollarbeträge, wenn
  der Nutzer in Euro arbeitet.
- **Denglisch sparsam:** "Learnings", "Mindset", "Gamechanger", "Deep Dive"
  nur, wenn sie in voice.md als eigene Wörter stehen.
- **Gendern** nach voice.md (Doppelpunkt, Sternchen, neutral oder gar nicht).
  Ohne Angabe: neutrale Formulierungen (Team, Mitarbeitende, wer ...).
- **Kein Behördendeutsch:** keine Nominalketten ("die Durchführung der
  Optimierung"), lieber Verben.

## Der Ablauf

**1. Drei Hooks, nicht einer.** Wähle aus `hooks.json` die drei Formeln, die
wirklich passen. Verschiedene Formeln, nicht drei Varianten einer. Als drei
nummerierte Zeilen, plus ein Satz, welchen du nehmen würdest und warum.

**2. Den ganzen Post** auf dem stärksten Hook schreiben.

**3. Humanisieren.** Den Entwurf durch `/li-human` jagen, bevor du ihn zeigst.
Jeder Post aus diesem Skill wird humanisiert ausgeliefert.

**4. Den Block ausgeben**, kopierfertig in einem Codeblock, genau so, wie er
eingefügt werden soll. Darunter:

```
POST BEREIT
Hook:       #17 Zeitanker
Länge:      1.240 Zeichen
Humanizer:  6 Artefakte entfernt, Human Score 84 PASS
Posten:     Dienstag 8:15 Uhr (laut Plan)

Antworte "ja", um ihn zu loggen, oder sag mir, was sich ändern soll.
```

**5. Nie veröffentlichen.** Dieser Skill produziert Text, der Nutzer postet.
Bei "ja" den Post in `~/.claude/linkedin/log.md` anhängen: Datum, Hook-Nummer,
erste Zeile, damit `/li-audit` später eine Historie hat.

## Regeln, die den Unterschied machen

- **Eine Idee pro Post.** Hat der Entwurf zwei, sind es zwei Posts. Sag das.
- **Zahlen statt Adjektive.** "4.200 €" schlägt "eine Menge". Fehlt die Zahl,
  frag danach, statt um das Loch herumzuschreiben.
- **Kein Engagement-Köder.** "Was meint ihr?" und "Seht ihr das auch so?" sind
  tot. Die Schlussfrage muss eine sein, die nur dieser Post stellen kann.
- **Höchstens drei Hashtags**, ganz unten, nur echte Kategorien.
- **Keine Links im Text.** LinkedIn drosselt Posts mit externen Links. Link in
  den ersten Kommentar, und sag das in der Quittung.
- **Nichts erfinden.** Keine ausgedachten Kennzahlen, Kunden, Umsätze oder
  Ergebnisse unter dem Namen des Nutzers, auch nicht als Platzhalter. Fehlt
  eine Zahl, bleibt `{{deine Zahl}}` im Entwurf stehen und wird markiert.

## Beispiel

```
/li-post wir haben ein internes Tool gebaut, das Angebote von 5 Stunden auf 20 Minuten bringt
```

```
HOOKS
1. #17 Zeitanker    Ein Angebot hat mich früher 5 Stunden gekostet. Heute 20 Minuten.
2. #12 Vergleich    12.000 € Agentur gegen ein Wochenende und eine Vorlage. Das Wochenende hat gewonnen.
3. #3  Fehler       Zwei Jahre lang habe ich Kunden Stunden berechnet, die ich mit Formatieren verbrannt habe.

Ich nehme #17: das Verhältnis ist glaubwürdig und die Zahl gehört dir.
```
