---
name: li-carousel
description: "Baut deutsche LinkedIn-Karussells: Folientext, Cover, Begleittext und PDF 1080x1350. Bei 'Karussell', 'Dokument-Post', 'Slides für LinkedIn'."
---

# li-carousel

Dokument-Posts haben auf LinkedIn die höchste Verweildauer, weil ein Wischen
zählt und ein Scrollen nicht. Das Format belohnt eine Idee in Schritten und
bestraft einen in Stücke geschnittenen Textpost.

## Wann statt eines Textposts

Bei **Abfolge**: Schritte, Countdown, Vorher/Nachher-Verlauf, ein Framework mit
Teilen. Ein Textpost bei einer einzigen Behauptung. Eine Behauptung auf acht
Folien verteilen ist der häufigste Fehler; hat der Nutzer das, sag es und
übergib an `/li-post`.

## Aufbau

8-12 Folien. Unter 8 ist es ein Textpost, über 12 bricht die Abschlussquote ein.

```
1        COVER      der Hook, höchstens 6 Wörter, plus eine Zeile Versprechen
2        DER EINSATZ warum das zählt, in einem Satz
3-N      EINE IDEE PRO FOLIE. Überschrift 3-7 Wörter, darunter höchstens
                    25 Wörter. Braucht eine Folie einen Absatz, sind es zwei.
N+1      ZUSAMMENFASSUNG alles als Liste, damit der Screenshot nützt
LETZTE   CTA        eine Aktion. Folgen, ein Stichwort kommentieren, oder der Link. Eine.
```

## Regeln für den Folientext

- **Folie 1 ist 80 % des Ergebnisses.** Sechs Wörter, groß. Deutsche
  Komposita brechen schlecht um: lieber "Angebote in 20 Minuten" als
  "Angebotserstellungsbeschleunigung".
- **Jede Folie nummerieren** (3/10).
- **Keine Folie ist ein Absatz.** Mehr als 25 Wörter: teilen.
- **Die Zusammenfassung wird gescreenshottet.** Sie muss allein stehen.
- **Handle des Nutzers auf jeder Folie**, klein, unten in der Ecke.
- **Deutsche Typografie im Bild ist erlaubt**: auf Folien dürfen „deutsche
  Anführungszeichen“ und echte Gedankenstriche stehen, der Humanizer gilt für
  den Begleittext, nicht für das Bild-PDF.

## Das PDF

LinkedIn will ein PDF, 1080x1350 (4:5) für maximale Fläche im Feed, unter
100 MB, unter 300 Seiten. Als HTML bauen und als PDF drucken:

```bash
# eine Seite pro Folie, 1080x1350, keine Ränder
# dann: Chrome headless --print-to-pdf, oder ein anderes HTML-zu-PDF
```

HTML mit einer `<section>` pro Folie, `width:1080px; height:1350px;
page-break-after:always`, eine Akzentfarbe, Schrift nicht kleiner als 28px.
Silbentrennung aktivieren (`lang="de"` und `hyphens:auto`), sonst sprengen
lange Wörter die Zeile. Gibt es im Projekt ein Design-System, das benutzen.

## Output

Zuerst der Folientext als nummerierte Liste, in zehn Sekunden lesbar. Dann der
**Begleittext**: ein Karussell braucht 2-3 Zeilen darüber, das ist der
eigentliche Hook im Feed. Beides durch `/li-human`. Das PDF erst bauen, wenn der
Nutzer den Text freigibt.

Nichts wird zu LinkedIn hochgeladen. Der Nutzer postet das PDF selbst.
