---
name: li-comment
description: "Schreibt deutsche Kommentare unter fremde LinkedIn-Posts, 9 Typen, nie 'Toller Beitrag'. Bei 'kommentier das', 'was schreibe ich drunter', Engagement-Runde."
---

# li-comment

Kommentieren ist der größte Hebel auf LinkedIn und am leichtesten schlecht zu
machen. Ein Kommentar unter einem Post mit 400 Reaktionen wird von mehr Leuten
gesehen als die meisten eigenen Posts. Ein generischer Kommentar wird von
niemandem gesehen und kostet Glaubwürdigkeit beim Autor.

## Input

Der Nutzer fügt den Text ein (und Name und Rolle des Autors, falls bekannt).
Screenshots sind ok. Bei einer URL, die du nicht öffnen kannst: um den Text
bitten. Nicht raten, was drinstand, und den Feed nicht per Browser auslesen.

## Anrede

Spiegel den Autor: duzt der Post seine Leser, duzt der Kommentar. Siezt er,
oder ist es erkennbar eine konservative Branche (Recht, Notariat, Banken,
Behörden), wird gesiezt. Im Zweifel voice.md, sonst Du.

## Die neun Kommentartypen

Wähle nach dem, was der Post tatsächlich ist. Nie standardmäßig Typ 1.

| # | Typ | wann | Form |
| --- | --- | --- | --- |
| 1 | **Datenpunkt** | Post behauptet etwas, das du mit einer Zahl stützen kannst | "Bei uns genauso: 40 % unserer ..." |
| 2 | **Der fehlende Fall** | richtig, aber unvollständig | "Gilt, bis {Bedingung}. Dann ..." |
| 3 | **Respektvoller Widerspruch** | du hältst es wirklich für falsch | erst die Zustimmung, dann die Abzweigung |
| 4 | **Eine Zeile weiterdenken** | ein Satz im Post ist der gute | zitieren, darauf aufbauen |
| 5 | **Die echte Frage** | der Post überspringt den schweren Teil | eine konkrete Frage, kein "Mich würde interessieren" |
| 6 | **Der Beleg** | du hast genau das gemacht | was passiert ist, in zwei Sätzen |
| 7 | **Die Korrektur** | ein sachlicher Fehler | richtig, kurz, freundlich, sicher |
| 8 | **Neu einordnen** | richtige Fakten, falscher Rahmen | "Man kann das auch so lesen:" |
| 9 | **Der Einzeiler** | der Post braucht nichts, du willst Präsenz | unter 12 Wörtern, witzig oder wahr |

## Regeln

- **2 bis 4 Sätze.** Länger wirkt wie Kapern, kürzer wie Füllstoff.
- **Nie** mit "Toller Beitrag", "Super Post", "Absolut!", "Danke fürs
  Teilen", "Spannend!", "Sehr wahr", "Kann ich nur unterschreiben" oder dem
  Vornamen des Autors plus Ausrufezeichen anfangen. Unsichtbar, alle.
- **Kein Emoji als erstes Zeichen.** Kein 🔥 oder 👏 am Anfang.
- **Den Post nie nacherzählen.** Der Autor weiß, was er geschrieben hat.
- **Eine Idee.** Zwei Punkte wirken wie ein Blogversuch.
- **Das Konkrete sagen.** Passt der Kommentar unter jeden Post zum Thema, ist
  er kein Kommentar, sondern Rauschen.
- **Widerspruch ist erlaubt und wirkt**, aber die Zustimmung kommt zuerst und
  muss echt sein.

## Output

**Zwei Optionen verschiedener Typen**, beschriftet, plus ein Satz, welche du
posten würdest. Beide vorher durch `/li-human`: ein Gedankenstrich fällt im
kurzen Kommentar noch mehr auf als im Post.

```
KOMMENTAR-OPTIONEN  (zu @autor, Post übers Recruiting)

[6 · Beleg]
Wir haben das ohne Lebenslauf letztes Jahr bei 3 Einstellungen probiert. Zwei
waren unsere besten Leute. Die dritte war ein Reinfall, und der Unterschied
war, ob sie den Job vorher schon gemacht hatten, nicht wie sie im Gespräch waren.

[3 · Respektvoller Widerspruch]
Beim Signal-Problem bin ich bei dir. Gelöst hat es bei uns aber nicht der
Verzicht auf den Lebenslauf, sondern eine bezahlte 90-Minuten-Aufgabe für alle.
Gleiches Ergebnis, deutlich weniger Diskussion intern.

Nimm die erste. Eigene Daten plus ein zugegebener Fehlschlag, darauf antworten Leute.
```

## Batch-Modus

Für eine Engagement-Runde 5-10 Posts als Text in einer Nachricht anfordern,
einen Kommentar pro Post in einem Block zurückgeben und in
`~/.claude/linkedin/log.md` notieren, wen der Nutzer diese Woche schon
kommentiert hat. Jeden Tag dieselben drei Leute ist sichtbar.

## Nie

Nicht automatisch posten. Keine Browser-Tools zum Veröffentlichen nutzen.
Automatisches Posten und Scraping verstoßen gegen die LinkedIn-Nutzervereinbarung
und gefährden das Konto. Dieser Skill schreibt, der Nutzer postet.
