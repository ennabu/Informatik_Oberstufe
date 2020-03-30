## Die Objektorientierte Brille

Setzen Informatiker\*innen ihre objektorientierte Brille auf, sehen sie nur noch **Objekte** , die zu irgendwelchen **Klassen** zusammen gefasst werden können. So gibt es zum Beispiel lauter unterschiedliche  Objekte (manchmal bezeichnet man sie auch als **Instanzen**), die alle der Klasse *Katze* angehören. 

Sie haben gemeinsame **Attribute**, also Eigenschaften und auch **Methoden**, die sie alle ausführen können (genauer: die man an ihnen vollziehen kann). Man stellt diese Informationen in einer **Klassenkarte** dar.

![Klassenkarte](img/Klassenkarte.png)

Einzelne Objekte aus dieser Klasse weisen nun die gleichen Attribute und Methoden auf, wie die Klasse – die **Attributwerte** sind aber unterschiedlich. 

![Grumpy](img/Grumpy.jpeg)

![katze1](img/katze1.png)



t> Lege Objektkarten für zwei weitere Objekte der Klasse Katze an.

t> Überlege dir zwei andere Beispiele für Objekte und Klassen.



## Datenkapselung

Eines der Grundprinzipien der Objektorientierten Modellierung ist die **Datenkapselung**. Dieses Prinzip sorgt dafür, dass der Zugriff auf Methoden und Attribute explizit durch die Klasse geregelt wird. Attribute und Methoden können entweder die Sichtbarkeit **private** (-) oder **public** (+) haben. Private bedeutet, dass das Attribut oder die Methode nur vom Objekt selbst verwendet werden kann – Public dass der Zugriff auch von außerhalb, beispielsweise durch ein anderes Objekt möglich ist.

Häufig kommt es beispielsweise vor, dass der Zugriff auf bestimmte Attribute nur über eine entsprechende Methode möglich ist. 

![katze_datenkapselung](img/katze_datenkapselung.png)

t> Überlege dir hinreichend plausible Gründe für die Wahl der Sichtbarkeiten im obigen Beispiel.

Aus dieser erweiterten Form der Klassenkarte gehen neben der Sichtbarkeit noch **Parameter** für einzelne Methoden und die **Datentypen** für die Attribute hervor. Die Methode *schlafe* erhält z.B. einen Integer-Wert, während die Methode *sageDeinenName* einen String-Wert zurückliefert. 

w> Du solltest die Bedeutung der Datentypen *Integer*, *Float*, *Boolean* und *String* kennen.

t> Formuliere Übergabe- und Rückgabewert für die übrigen Methoden.



## Vererbung, Generalisierung und Spezialisierung

Ausgehend von einer bestehenden allgemeinen **Klasse** kann man verwandte Klassen definieren. Die so entstehende **abgeleitete Klasse** erbt Methoden und Attribute der **Basisklasse**. Ableleitete Klassen haben womöglich weitere oder veränderte Eigenschaften. 

![Vererbung2](img/Vererbung2.png)

Die abgeleitete Klasse hat damit nicht nur alle Attribute der Klasse *Katze*, sondern auch zusätzliche wie z.B. eine Farbe. Bei den Methoden verhält es sich ähnlich. 

Im obigen Beispiel ist die Klasse *Katze* eine **Generalisierung** der Klassen *ComicKatze* und *Hauskatze*, während umgekehrt die Klassen *ComicKatze* und *Hauskatze* eine **Spezialisierung** der Klasse *Katze* sind.

t> Überlege dir für deine oben gewählten Beispielszenarien mögliche Generalisierungen oder Spezialisierungen deiner Klassen.

