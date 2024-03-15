"""For this challenge, you need to create a multi-function calculator using Python that take input and do the following:

solve proportions
solve for x in equations
factor square roots
convert decimals to fractions and percents
convert fractions to decimals and percents
convert percents to decimals and fractions"""
import time,re,math
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, solve, factor,sympify,pprint,sqrt as sqrt_from_sympy


def show_menu():
    print("Select one of the following operations:")
    print("1) Solve proportions")
    print("2) Solve for x in equations")
    print("3) Factor square roots")
    print("4) Convert decimals to fractions and percents")
    print("5) Convert fractions to decimals and percents")
    print("6) Convert percents to decimals and fractions")
    print("7) Exit")

def solve_proportions(n1, d1, n2, d2):
    variables = [n1, d1, n2, d2]
    countOfUnknowns = 0

    for variable in variables:
        if isinstance(variable, str) and not variable.isdigit():
            countOfUnknowns += 1
            if countOfUnknowns == 2:
                return "Invalid operation, more than 1 unknown"

    if not n1.isdigit():
        answer = float(d1) * float(n2) / float(d2)
        return "Solution:" + n1 + "=" + str(answer)
    if not n2.isdigit():
        answer = float(n1) * float(d2) / float(d1)
        return "Solution:" + n2 + "=" + str(answer)
    if not d1.isdigit():
        answer = float(n1) * float(d2) / float(n2)
        return "Solution:" + d1 + "=" + str(answer)
    if not d2.isdigit():
        answer = float(d1) * float(n2) / float(n1)
        return "Solution:" + d2 + "=" + str(answer)

    # If all vars are nums (there is not an unknown)
    return "No unknowns"
def solve_for_x(left, right, zero_syntax_eq):
    if zero_syntax_eq:
        equation = Eq(sympify(right), 0)
    else:
        equation = Eq(sympify(right), symbols('y'))

    solution = solve(equation, symbols('x'))

    if solution:
        print("Solutions for x:")
        for s in solution:
            print("x =", s)
    else:
        print("No solution found for x.")


def factor_square_roots(num):
    upper_limit = math.floor(math.sqrt(num)) + 1
    max_factor = 1

    for maybe_factor in range(1, upper_limit):
        if num % (maybe_factor ** 2) == 0:
            max_factor = maybe_factor ** 2

    other_factor = num / max_factor
    square_root = sqrt_from_sympy(max_factor)

    return str(square_root)+"*"+"sqrt("+str(other_factor)+")"


while True:
    show_menu()
    option = input("Enter your choice: ")
    match option:
        case "1":
            print("** solve proportions **")
            proportions = input(
                'Insert a proportion with the follow format n1/d1=n2/d2.\nReplace 3 of them with values and leave the unknown as a letter like X.Example input: 3/5=4/x\n')
            if "=" in proportions:
                left, right = proportions.split("=")
                if "/" in left and "/" in right:
                    n1, d1 = left.split("/")
                    n2, d2 = right.split("/")
                    print(solve_proportions(n1, d1, n2, d2))
                else:
                    print("Invalid format")
            else:
                print("Invalid format")
            time.sleep(1.5)
        case "2":
            print('** Solve for x in equations **')
            equation = input("Insert an equation in terms of x and y to solve for x.\nExamples: y=x*2+1, 0=2*x-y\n")
            if "=" in equation:
                left, right = equation.split("=")
                if "y" in left:
                    solve_for_x(left, right.strip(), False)
                elif "0" in left:
                    solve_for_x(left.strip(), right.strip(), True)
                else:
                    print("Invalid format: Equation should have 'y' on the left or '0' on the left.")
            else:
                print("Invalid format: Equation should have '='.")
            time.sleep(1.5)
        case "3":
            pattern_sqrt = r"\((\d+(?:\.\d+)?)\)"
            print("** factor square roots **")
            numStr = input("Insert the num of the square root for factor. format: 1)sqrt(num) 2) just write the num\n")
            result_for_sqrt = re.search(pattern_sqrt, numStr)
            if result_for_sqrt:
                num = float(result_for_sqrt.group(1))
                output = factor_square_roots(num)
                pprint(output)
            elif isinstance(numStr, str) and numStr.isdigit():
                output = factor_square_roots(float(numStr))
                pprint(output)
            else:
                print("Invalid format for the option choosed")
            time.sleep(1.5)
        case "4":
            print("** convert decimals to fractions and percents **")
            # Tu lógica para convertir decimales a fracciones y porcentajes aquí
        case "5":
            print("** convert fractions to decimals and percents **")
            # Tu lógica para convertir fracciones a decimales y porcentajes aquí
        case "6":
            print("** convert percents to decimals and fractions **")
            # Tu lógica para convertir porcentajes a decimales y fracciones aquí
        case "7":
            break
        case _:
            print("Select a valid operation")
            continue
