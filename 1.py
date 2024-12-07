# Завдання на використання функцій з бібліотекою math (середній рівень):

# 1.Площа кола
# Напишіть функцію, яка обчислює площу кола за заданим радіусом.

import math

def area_of_a_circle(r):
    return math.pi * r ** 2

radius = float(input("Введіть радіус кола:"))

print(f"S кола =", area_of_a_circle(radius))