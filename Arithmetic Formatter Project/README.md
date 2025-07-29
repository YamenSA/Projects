# 🧮 Arithmetic Formatter

Dieses Python-Tool formatiert einfache Rechenaufgaben (Addition und Subtraktion) vertikal nebeneinander – wie man sie handschriftlich schreiben würde. Optional können auch die Ergebnisse angezeigt werden.

---

## ✨ Funktionen

- Unterstützt Addition (`+`) und Subtraktion (`-`)
- Validierung:
  - Maximal 5 Aufgaben
  - Nur Ziffern (max. 4-stellig)
  - Kein `*` oder `/`
- Optional: Ausgabe mit Lösungen
- Klar lesbare Konsolen-Ausgabe, z. B.:

```python
   44      909      45      123      888
+ 815    -   2    + 43    +  49    +  40
-----    -----    ----    -----    -----
  859      907      88      172      928
```

---

## 🚀 Verwendung

```python
from arithmetic_formatter import arithmetic_arranger

print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43"], show_answers=True))
```

### Ausführen als Skript:

```bash
python arithmetic_formatter.py
```

---

## 🛠️ Hintergrund

Das Projekt entstand als Übung zur Verbesserung meiner Python-Kenntnisse in Bezug auf String-Manipulation, Eingabevalidierung und funktionale Struktur.  
Die Idee basiert auf einer Aufgabenstellung von [freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-an-arithmetic-formatter-project/build-an-arithmetic-formatter-project), wurde jedoch eigenständig entwickelt und erweitert.

---

## 👤 Autor

**Yamen Sandakli**

Weitere Ideen zur Weiterentwicklung:
- Unterstützung weiterer Operatoren (×, ÷)
- Kommandozeilenargumente für flexible Nutzung
- Web-Interface zur Visualisierung
