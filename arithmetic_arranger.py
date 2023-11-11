def arithmetic_arranger(problems, showanswer=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    results = {"first": "", "second": "", "third": "", "solution": ""}

    for problem in problems:
        operands = problem.split()
        if len(operands) != 3:
            return f"Error: '{problem}' is not properly formatted. It may contain extra space."

        num1, operator, num2 = operands

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        try:
            num1, num2 = int(num1), int(num2)
            if abs(num1) > 9999 or abs(num2) > 9999:
                return "Error: Numbers cannot be more than four digits."
        except ValueError:
            return "Error: Numbers must only contain digits."

        width = max(len(str(num1)), len(str(num2))) + 2
        results["first"] += f"{num1:>{width}}    "
        results["second"] += f"{operator} {num2:>{width-2}}    "
        results["third"] += "-" * width + "    "

        total = num1 + num2 if operator == "+" else num1 - num2
        results["solution"] += f"{total:>{width}}    "

    # for key in results:
    #     results[key] = results[key].rstrip()

    if showanswer:
        return "\n".join(results[key].rstrip() for key in results)
    else:
        return "\n".join([results[key].rstrip() for key in ["first", "second", "third"]])

