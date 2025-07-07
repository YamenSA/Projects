# 🧮 Arithmetic Formatter (freeCodeCamp Projekt)

Dieses Projekt ist die Lösung zur Übung **"Arithmetic Formatter"** aus dem Python-Kurs von [freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-an-arithmetic-formatter-project/build-an-arithmetic-formatter-project).  
Die Aufgabe besteht darin, mehrere einfache Rechenaufgaben sauber nebeneinander zu formatieren – optional mit Ergebnissen.

---

## ✅ Funktionen

- Unterstützt nur Addition (`+`) und Subtraktion (`-`)
- Prüft:
  - Maximal 5 Aufgaben erlaubt
  - Nur Ziffern erlaubt (keine Buchstaben, Sonderzeichen)
  - Operanden dürfen maximal 4 Ziffern lang sein
- Formatiert jede Aufgabe vertikal, rechtsbündig
- Gibt optional die Ergebnisse darunter aus

---

## 💻 Beispiel

```python
from arithmetic_formatter import arithmetic_arranger

print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40"], show_answers=True))

   44      909      45      123      888
+ 815    -   2    + 43    +  49    +  40
-----    -----    ----    -----    -----
  859      907      88      172      928
```

## 📌 Verwendung
1. Stelle sicher, dass Python installiert ist.
2. Öffne das Projekt in VS Code oder einem beliebigen Editor.
3. Führe arithmetic_formatter.py aus:

```bash 
python arithmetic_formatter.py
```

## ⚠️ Einschränkungen
- Multiplikation (*) und Division (/) sind nicht erlaubt
- Mehr als 5 Aufgaben führen zu einem Fehler
- Die Formatierung erfolgt ohne Lösung, außer show_answers=True

## ✍️ Autor
- Yamen Sandakli
- Dieses Projekt wurde im Rahmen des Python-Kurses von freeCodeCamp.org umgesetzt.

