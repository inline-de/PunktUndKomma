# PunktUndKomma
Wir sagen vorraus, welches Zeichen in einer Kette von Wörter nach dem sechstletzten und vor dem fünftletzten Wort das richtige wäre, z.B. ",", ".", "!", "?".

Er schafft es leider noch nicht so zuverlässig, die Satzzeichen sicher vorherzusagen, aber man kann meistens einen deutlichen Anstieg der Wahrscheinlichkeit des richtigen Zeichens sehen. Trotzdem ist die Wahrscheinlichkeit des Leerzeichens meistens noch größer.

Unsere Probleme waren u.a. das Finden eines geeigneten Datensatzes und das Trainieren auf einem Datensatz, den unsere Hardware verträgt, die aber trotzdem groß genug ist. So wirklich hat das nicht geklappt, für vernünftige Ergebnisse bräuchten wir mehr.

# Beispiel

> Mir stießen Tränen in die Augen Tim schaute mich an "Was ist los" fragte er überrascht "Ach nichts>> <<Ich habe nur grade nachgedacht

```
 [Kein Satzzeichen] =      34.17 
                  . =      44.01 actual - predicted
                  , =      -8.12 
                  ! =      -1.98 
                  ? =     -15.65
```
