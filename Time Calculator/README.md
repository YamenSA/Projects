\# Zeitrechner (Time Calculator)



Ein kleines Python-Projekt, das eine Startzeit und eine Dauer addiert. Es zeigt das Ergebnis im 12-Stunden-Format an und berechnet, wie viele Tage vergangen sind, einschließlich der Aktualisierung des Wochentags (falls angegeben).



\### Features



\* ✅ Addiert Stunden und Minuten zur Startzeit.

\* ✅ Konvertiert korrekt zwischen AM und PM.

\* ✅ Fügt den Zusatz `(next day)` oder `(n days later)` hinzu.

\* ✅ Berechnet den korrekten Wochentag, wenn ein Starttag angegeben wird (z.B. Montag + 48 Stunden = Mittwoch).



\### Installation und Nutzung



Dieses Projekt benötigt keine externen Bibliotheken und kann direkt ausgeführt werden.



1\.  \*\*Repository klonen:\*\*

&nbsp;   ```bash

&nbsp;   git clone \[https://github.com/DEIN-BENUTZERNAME/DEIN-REPO-NAME.git](https://github.com/DEIN-BENUTZERNAME/DEIN-REPO-NAME.git)

&nbsp;   cd DEIN-REPO-NAME

&nbsp;   ```



2\.  \*\*Code ausführen:\*\*

&nbsp;   ```bash

&nbsp;   python add\_time.py

&nbsp;   ```



\### Funktionsaufruf



Die Hauptfunktion ist `add\_time(start, duration, day=None)`. Hier sind Beispiele für die Verwendung in Python:



```python

add\_time('3:00 PM', '3:10')

\# Returns: '6:10 PM'



add\_time('11:43 PM', '24:20', 'tueSday')

\# Returns: '12:03 AM, Thursday (2 days later)'



\### Beispiele



| Startzeit | Dauer | Optionaler Tag | Ergebnis |

| :--- | :--- | :--- | :--- |

| '3:00 PM' | '3:10' | | 6:10 PM |

| '11:30 AM' | '2:32' | 'Monday' | 2:02 PM, Monday |

| '10:10 PM' | '3:30' | | 1:40 AM (next day) |

| '6:30 PM' | '205:12' | | 7:42 AM (9 days later) |





