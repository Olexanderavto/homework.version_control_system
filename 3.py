# 3.	Квадратне рівняння
# Напишіть функцію, яка знаходить корені квадратного рівняння ax2+bx+c=0ax^2 + bx + c = 0
# за допомогою math.sqrt

import math

def equation(a, b, c):
    if a == 0:
        return "Помилка: Це не квадратне рівняння, оскільки a = 0."

    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return f"Два дійсних корені: x1 = {x1}, x2 = {x2}"
    elif D == 0:
        x = -b / (2 * a)
        return f"Один дійсний корінь: x = {x}"
    else:
        return "Немає дійсних коренів (дискримінант < 0)."

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

print(equation(a, b, c))
