# 9.	Знаходження гіпотенузи

# Напишіть функцію, яка обчислює гіпотенузу прямокутного трикутника за його катетами.

import math

def calculate_hypotenuse(a, b):
    """
    Обчислює гіпотенузу прямокутного трикутника.

    :param a: Довжина першого катета
    :param b: Довжина другого катета
    :return: Довжина гіпотенузи
    """
    if a <= 0 or b <= 0:
        raise ValueError("Довжини катетів повинні бути більшими за 0")
    return math.sqrt(a**2 + b**2)

# Приклад використання
cathetus1 = 3
cathetus2 = 4
print(f"Гіпотенуза трикутника з катетами {cathetus1} і {cathetus2} = {calculate_hypotenuse(cathetus1, cathetus2)}")
