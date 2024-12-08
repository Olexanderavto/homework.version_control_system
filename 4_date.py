# 4.	Перевірка високосного року

# Реалізуйте функцію, яка визначає, чи є рік високосним.

def is_leap_year(year):
    """
    Перевіряє, чи є рік високосним.

    Параметри:
    year (int): Рік для перевірки.

    Повертає:
    bool: True, якщо рік високосний, інакше False.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Приклади використання:
print(is_leap_year(2024))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True
