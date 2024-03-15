"""For this challenge, you need to create a multi-function calculator using Python that take input and do the following:

solve proportions
solve for x in equations
factor square roots
convert decimals to fractions and percents
convert fractions to decimals and percents
convert percents to decimals and fractions"""

import time
import matplotlib.pyplot as plt
import numpy as np
import math
import sympy
from sympy import symbols
from sympy.solvers import solve
from sympy import factor


def show_menu():
    print("Select one of the following operations:")
    print("1) Solve proportions")
    print("2) Solve for x in equations")
    print("4) Factor square roots")
    print("5) Convert decimals to fractions and percents")
    print("6) Convert fractions to decimals and percents")
    print("7) Convert percents to decimals and fractions")
    print("8) Exit")


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
                    time.sleep(1.5)
                else:
                    print("Invalid format")
            else:
                print("Invalid format")
        case "2":
            print("** solve for x in equations **")
            # Tu lógica para resolver ecuaciones con x aquí
        case "4":
            print("** factor square roots **")
            # Tu lógica para factorizar raíces cuadradas aquí
        case "5":
            print("** convert decimals to fractions and percents **")
            # Tu lógica para convertir decimales a fracciones y porcentajes aquí
        case "6":
            print("** convert fractions to decimals and percents **")
            # Tu lógica para convertir fracciones a decimales y porcentajes aquí
        case "7":
            print("** convert percents to decimals and fractions **")
            # Tu lógica para convertir porcentajes a decimales y fracciones aquí
        case "8":
            break
        case _:
            print("Select a valid operation")
            continue
