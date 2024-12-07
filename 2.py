# 2.	Обчислення факторіалу
# Реалізуйте функцію, яка використовує math.factorial для обчислення факторіала числа.

import math

def factorial():
    return math.factorial(num)

num = int(input("Введіть число:"))

print(f"факторіала числа {num} =",factorial())