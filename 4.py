# 4.	Довжина дуги кола
# Реалізуйте функцію, яка знаходить довжину дуги кола для заданого радіуса і кута в радіанах.

import math


def arc_length(radius, angle_in_radians):
    """
    Обчислює довжину дуги кола.

    Параметри:
    radius (float): Радіус кола.
    angle_in_radians (float): Кут в радіанах.

    Повертає:
    float: Довжина дуги.
    """
    if radius < 0:
        raise ValueError("Радіус не може бути від'ємним.")
    if angle_in_radians < 0:
        raise ValueError("Кут у радіанах має бути невід'ємним.")

    return radius * angle_in_radians


# Приклад використання
r = 5  # радіус
theta = 1.2  # кут у радіанах
print("Довжина дуги:", arc_length(r, theta))