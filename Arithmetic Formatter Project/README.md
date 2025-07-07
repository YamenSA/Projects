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
```
