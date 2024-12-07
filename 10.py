# 10.	Перетворення декартових координат у полярні

# Функція приймає координати точки (x,y)(x, y) і повертає їх у полярній системі
# за допомогою math.atan2 і math.sqrt.

import math

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)  # радіус
    theta = math.atan2(y, x)  # кут в радіанах
    return r, theta

# Приклад використання
x = 3
y = 4
r, theta = cartesian_to_polar(x, y)
print(f"Радіус: {r}, Кут: {theta} радіан")
