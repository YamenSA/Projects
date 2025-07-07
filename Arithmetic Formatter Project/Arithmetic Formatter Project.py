def arithmetic_arranger(problems, show_answers=False):
    sorted = []
    operator = []
    dashes = []
    solved = []
    if (len(problems)) > 5:
        return "Error: Too many problems."
    elif operator_checker(problems) == False:
        return "Error: Operator must be '+' or '-'."
    elif digit_checker(problems) == False:
        return "Error: Numbers must only contain digits."
    elif digit_length_checker(problems) == False:
        return "Error: Numbers cannot be more than four digits."
    else:

        if show_answers == True:

            for problem in problems:
                i = 0
                g = 1
                h = 2

                operands = problem.split()
                spaltenbreite = max(len(operands[i]), len(operands[h])) + 2
                sorted.append(operands[i].rjust(spaltenbreite))
                operator.append(operands[g] + operands[h].rjust(spaltenbreite - 1))
                if len(operands[i]) < len(operands[h]):
                    dashes.append("-" * (len(operands[h]) + 2))
                else:
                    dashes.append("-" * (len(operands[i]) + 2))

                if operands[1] == "+":
                    solved.append(
                        str(int(operands[i]) + int(operands[h])).rjust(spaltenbreite)
                    )
                else:
                    solved.append(
                        str(int(operands[i]) - int(operands[h])).rjust(spaltenbreite)
                    )

            result = "    ".join(sorted)
            result1 = "    ".join(operator)
            result2 = "    ".join(dashes)
            result3 = "    ".join(solved)

            resultfinal = result + "\n" + result1 + "\n" + result2 + "\n" + result3

            return resultfinal
        else:

            for problem in problems:
                i = 0
                g = 1
                h = 2

                operands = problem.split()
                spaltenbreite = max(len(operands[i]), len(operands[h])) + 2
                sorted.append(operands[i].rjust(spaltenbreite))
                operator.append(operands[g] + operands[h].rjust(spaltenbreite - 1))
                if len(operands[i]) < len(operands[h]):
                    dashes.append("-" * (len(operands[h]) + 2))
                else:
                    dashes.append("-" * (len(operands[i]) + 2))

                # if operands[1] == "+":
                #     solved.append(
                #         str(int(operands[i]) + int(operands[h])).rjust(spaltenbreite)
                #     )
                # else:
                #     solved.append(
                #         str(int(operands[i]) - int(operands[h])).rjust(spaltenbreite)
                #     )

                result = "    ".join(sorted)
                result1 = "    ".join(operator)
                result2 = "    ".join(dashes)
            # result3 = "    ".join(solved)

            resultfinal = result + "\n" + result1 + "\n" + result2  # + result3

    return resultfinal


def operator_checker(problems):
    for problem in problems:
        if "*" in problem or "/" in problem:
            return False
    return True


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


def main():
    print(
        arithmetic_arranger(
            ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]
        )
    )


main()
