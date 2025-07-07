from Arithmetic_Formatter_Project import arithmetic_arranger


def test_arithmetic_arranger():
    # Test 1: Normalfall
    result = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
    expected = (
        "    3      3801      45      123\n"
        "+ 855    -    2    +  43    +  49\n"
        "-----    ------    ----    -----"
    )
    assert result == expected, "Test 1 fehlgeschlagen"

    # Test 2: Mehr als 5 Aufgaben
    result = arithmetic_arranger(["1 + 2", "1 + 2", "1 + 2", "1 + 2", "1 + 2", "1 + 2"])
    assert result == "Error: Too many problems.", "Test 2 fehlgeschlagen"

    # Test 3: Ungültiger Operator
    result = arithmetic_arranger(["1 + 2", "1 * 2"])
    assert result == "Error: Operator must be '+' or '-'.", "Test 3 fehlgeschlagen"

    # Test 4: Ungültige Ziffern
    result = arithmetic_arranger(["3 + ab"])
    assert result == "Error: Numbers must only contain digits.", "Test 4 fehlgeschlagen"

    # Test 5: Operand zu lang
    result = arithmetic_arranger(["12345 + 6789"])
    assert (
        result == "Error: Numbers cannot be more than four digits."
    ), "Test 5 fehlgeschlagen"

    print("Alle Tests erfolgreich bestanden ✅")


if __name__ == "__main__":
    test_arithmetic_arranger()
