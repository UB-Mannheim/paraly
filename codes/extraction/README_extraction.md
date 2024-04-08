# Text extraction

The extraction scripts are created by [Dr. Jan Oliver Rüdiger](https://notes.jan-oliver-ruediger.de/ueber-mich/) and adapted for his software [CorpusExplorer](https://notes.jan-oliver-ruediger.de/software/corpusexplorer-overview/). He also provided the output data.

This folder contains the following files:

* Skript.cecs – Ein CorpusExplorer-Skript
* Query.txt Wichtig: Die erste Zeile lautet SPAN-1 – d.h. Es wird nur der Satz ausgegeben, der vor der Fundstelle steht. Die zweite Zeile lautet SPAN+1 als der Satz nach der Fundstelle. Wenn man mehr Text braucht, dann erhöhe den Wert z. B. auf SPAN-3 und SPAN+5. Die anderen Zeilen sollten deine Suchabfrage enthalten. Man kann einzelne Token oder exakte Token-Folgen „Dank an“ schreiben. Pro Zeile immer eine Abfrage.
* Starten.bat – Die startet das Skript, das Query.txt nutzt. Wichtig: man muss vorher ein Korpus in den Ordner legen, indem auch skript.cec, query.txt und starten.bat liegen. Diese Datei muss den Namen ‚corpus‘ tragen. Z. B. corpus.cec6 oder corpus.cec6.lz4 – Also bitte den Dateinamen ändern. Das Skript braucht ein paar Sekunden und es extrahiert die die Belege. Die aber nur mit GUID. Bitte beachten: Im Ordner wird eine neue TSV-Datei erstellt ‚output.tsv‘ wenn man das Skript mehrfach ausführt, muss man den Output zuvor löschen oder in einen anderen Ordner verschieben. Sonst funktioniert das Skript nicht.
