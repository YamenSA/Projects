"""
arithmetic_formatter.py

Autor: [Dein Name oder GitHub-Handle]
Beschreibung:
    Dieses Skript implementiert die Lösung für das "Arithmetic Formatter"-Problem aus dem freeCodeCamp Python-Kurs.
    Die Funktion `arithmetic_arranger` formatiert eine Liste von Rechenaufgaben in Spaltenform mit optionaler Lösung.
    Unterstützte Operatoren: '+' und '-'.
    Es werden diverse Eingabevalidierungen durchgeführt, z. B. max. 5 Aufgaben, nur Ziffern, max. 4-stellige Zahlen.

Funktionen:
    - arithmetic_arranger(problems, show_answers=False)
    - operator_checker(problems)
    - digit_checker(problems)
    - digit_length_checker(problems)

Beispiel:
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)

"""


def arithmetic_arranger(problems, show_answers=False):
    # Zeileninhalte vorbereiten
    sorted = []
    operator = []
    dashes = []
    solved = []

    # Eingabevalidierung
    if len(problems) > 5:
        return "Error: Too many problems."
    elif operator_checker(problems) == False:
        return "Error: Operator must be '+' or '-'."
    elif digit_checker(problems) == False:
        return "Error: Numbers must only contain digits."
    elif digit_length_checker(problems) == False:
        return "Error: Numbers cannot be more than four digits."

    else:
        # Wenn show_answers aktiviert ist, berechne auch die Lösung jeder Aufgabe
        if show_answers == True:
            for problem in problems:
                operands = problem.split()
                spaltenbreite = max(len(operands[0]), len(operands[2])) + 2

                # Erste Zahl (oben), rechtsbündig
                sorted.append(operands[0].rjust(spaltenbreite))

                # Operator + zweite Zahl (unten), korrekt ausgerichtet
                operator.append(operands[1] + operands[2].rjust(spaltenbreite - 1))

                # Trennlinie
                dashes.append("-" * spaltenbreite)

                # Berechnung
                if operands[1] == "+":
                    solved.append(
                        str(int(operands[0]) + int(operands[2])).rjust(spaltenbreite)
                    )
                else:
                    solved.append(
                        str(int(operands[0]) - int(operands[2])).rjust(spaltenbreite)
                    )

            # Zeilen zusammenbauen
            result = "    ".join(sorted)
            result1 = "    ".join(operator)
            result2 = "    ".join(dashes)
            result3 = "    ".join(solved)

            resultfinal = result + "\n" + result1 + "\n" + result2 + "\n" + result3
            return resultfinal

        # Wenn show_answers = False, gib nur die Formatierung ohne Ergebnis aus
        else:
            for problem in problems:
                operands = problem.split()
                spaltenbreite = max(len(operands[0]), len(operands[2])) + 2

                sorted.append(operands[0].rjust(spaltenbreite))
                operator.append(operands[1] + operands[2].rjust(spaltenbreite - 1))
                dashes.append("-" * spaltenbreite)

            result = "    ".join(sorted)
            result1 = "    ".join(operator)
            result2 = "    ".join(dashes)

            resultfinal = result + "\n" + result1 + "\n" + result2
            return resultfinal


# Prüft, ob alle Operatoren gültig sind ('+' oder '-')
def operator_checker(problems):
    for problem in problems:
        if "*" in problem or "/" in problem:
            return False
    return True


# Prüft, ob alle Operanden aus Ziffern bestehen
def digit_checker(problems):
    for problem in problems:
        operands = problem.split()
        for op in operands:
            if op.isdigit():
                continue
            elif op == "+" or op == "-":
                continue
            else:
                return False
    return True


# Prüft, ob kein Operand mehr als 4 Ziffern hat
def digit_length_checker(problems):
    if digit_checker(problems):
        for problem in problems:
            operands = problem.split()
            for op in operands:
                if op == "+" or op == "-":
                    continue
                elif len(op) < 5:
                    continue
                else:
                    return False
    return True


# Beispielhafte Ausführung
def main():
    print(
        arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40"])
    )


if __name__ == "__main__":
    main()
