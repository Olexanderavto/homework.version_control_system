# 6.	Обчислення косинуса кута
# Функція приймає кут у градусах і повертає його косинус за допомогою math.cos.

import math

def cos_of_angle(degrees):
    """
    Обчислює косинус кута у градусах.

    :param degrees: Кут у градусах
    :return: Косинус кута
    """
    radians = math.radians(degrees)  # Перетворення градусів у радіани
    return math.cos(radians)

# Приклад використання
angle = 60  # Задайте кут у градусах
print(f"Косинус кута {angle}°: {cos_of_angle(angle)}")