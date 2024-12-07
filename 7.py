# 7.	Перевірка на просте число

# Реалізуйте функцію, яка перевіряє, чи є число простим,
# використовуючи math.sqrt для оптимізації перевірки дільників.

import math

def prime_number(n):
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 і 3 є простими числами
    if n % 2 == 0 or n % 3 == 0:
        return False  # Виключаємо парні числа та кратні трьом

        # Перевіряємо дільники до квадратного кореня з n
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):  # Перевіряємо числа виду 6k ± 1
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


# Приклад використання
number = 29  # Задайте число
print(f"Число {number} просте: {prime_number(number)}")