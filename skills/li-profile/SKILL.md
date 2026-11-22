---
name: li-profile
description: "Bewertet ein LinkedIn-Profil (100 Punkte, 12-Punkte-Rubrik) und schreibt Headline, Info, Erfahrung neu, auf Deutsch. Bei 'optimier mein Profil', 'neue Headline'."
---

# li-profile

Ein Profil ist kein Lebenslauf. Der Lebenslauf beantwortet "was hast du
gemacht". Das Profil beantwortet "soll ich dieser Person schreiben", und zwar
in etwa vier Sekunden, aus Headline und den ersten zwei Zeilen des Info-Texts.

## Input

Bitte um: Headline, Info-Abschnitt ("Info"/"About"), aktuelle Position und die
letzten zwei Stationen, plus ob es ein Banner und einen Abschnitt "Im Fokus"
(Featured) gibt. Ein Screenshot der oberen Karte reicht für den ersten Durchgang.
Nicht im Namen des Nutzers bei LinkedIn einloggen.

Die deutsche Oberfläche heißt teils anders als die englische; nenne beide
Namen, wenn du Abschnitte erwähnst (z. B. "Im Fokus / Featured").

## Bewerten

Lies `rubric.json` in diesem Ordner. Zwölf Punkte, 100 Punkte gesamt, jeweils
mit Beschreibung der vollen Punktzahl. Jeden Punkt bewerten, Tabelle zeigen,
Summe nennen. Ehrlich: die meisten Profile landen im ersten Durchgang bei 30
bis 45. Eine großzügige Bewertung ist nutzlos.

```
PROFIL-SCORE  41/100

  Headline              3/12   nur Jobtitel, kein Ergebnis, keine Zielgruppe
  Info, erste 2 Zeilen  2/10   beginnt mit "Mit Leidenschaft ..."
  Info, Rest            4/10   Werdegang statt Angebot
  Im Fokus              0/8    leer
  Banner                0/6    Standard-Blau
  ...
```

## Dann neu schreiben, in dieser Reihenfolge

Nach verlorenen Punkten absteigend. Nicht alles auf einmal, der Nutzer muss
jedes Stück selbst einfügen.

**1. Headline (220 Zeichen).** Formel: `{was du für wen tust} | {Beleg} |
{wie man startet}`. Nicht der Jobtitel. Nicht "Ich helfe X, Y zu ..." als die
ersten Wörter, so fängt inzwischen jedes zweite Profil an. Drei Optionen.

**2. Info, die ersten zwei Zeilen.** Alles danach steckt mobil hinter "mehr
anzeigen". Diese zwei Zeilen müssen sagen, wem du hilfst und was sich ändert.
Kein "mit Leidenschaft", kein "ergebnisorientiert", kein "Als erfahrener ...",
keine Bio in der dritten Person, nicht mit dem eigenen Namen anfangen.

**3. Info, Rest.** An eine Leserin, einen Leser geschrieben, in der Anrede aus
voice.md (Du oder Sie, nicht gemischt). Aufbau: ihr Problem, was du dagegen
tust, ein Beleg mit Zahl, was als Nächstes zu tun ist. Unter 1.600 Zeichen,
obwohl 2.600 erlaubt sind.

**4. Im Fokus.** Drei Einträge: der beste Post, ein Beleg (Case, Referenz,
Ergebnis), der Kontaktweg. Ein leerer Abschnitt kostet acht Punkte und ist der
einzige Teil des Profils, den du komplett steuerst.

**5. Berufserfahrung.** Jede Station: eine Zeile Verantwortungsbereich, dann
zwei bis drei Ergebnisse mit Zahlen, keine Aufgabenbeschreibungen ("zuständig
für ..."). Alles älter als zehn Jahre auf eine Zeile kürzen.

**6. Banner.** Ein Satz Positionierung und ein Kontaktweg. Das Standard-Blau
ist das deutlichste Signal, dass niemand zu Hause ist.

## Deutschland-spezifisch

- **Impressum:** Wer LinkedIn geschäftlich nutzt (Selbstständige,
  Unternehmer, Vertrieb fürs eigene Unternehmen), braucht in Deutschland in
  der Regel eine leicht erreichbare Anbieterkennzeichnung. Üblich ist ein Link
  "Impressum" in den Kontaktinfos (Website-Feld). Weise darauf hin, wenn er
  fehlt; das ist ein Hinweis, keine Rechtsberatung.
- **Zahlen und Titel deutsch:** 4.200 €, 30 %, "Geschäftsführer" statt "CEO",
  wenn die Zielgruppe deutsch ist; Englisch nur, wenn die Zielgruppe es ist.

## Output

Score-Tabelle, dann die Neufassungen als kopierfertige Blöcke in der
Reihenfolge der Behebung, jeweils durch `/li-human` gelaufen. Am Ende neu
bewerten und das Delta ehrlich zeigen: kommt die Neufassung auf 88 statt 98,
sag 88, und was die restlichen Punkte brauchen (meist Empfehlungen, ein echtes
Banner und Aktivität, nichts davon kann ein Text erzeugen).

Dieser Skill speichert nichts bei LinkedIn. Der Nutzer fügt jeden Abschnitt selbst ein.
