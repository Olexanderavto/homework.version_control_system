# 7.	День тижня для дати

# Реалізуйте функцію, яка повертає день тижня для заданої дати.

from datetime import datetime


def get_day_of_week(date_string):
    """
    Повертає день тижня для заданої дати.

    Параметри:
    date_string (str): Дата у форматі 'DD-MM-YYYY'

    Повертає:
    str: Назва дня тижня українською мовою.
    """
    # Перетворення рядка в об'єкт datetime
    date_object = datetime.strptime(date_string, '%d-%m-%Y')

    # Українські назви днів тижня
    days_of_week = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П’ятниця', 'Субота', 'Неділя']

    # Отримання індексу дня тижня (0 - понеділок, 6 - неділя)
    day_index = date_object.weekday()

    # Повернення відповідного дня тижня
    return days_of_week[day_index]


# Приклад використання:
date = '12-12-2024'
print(f"День тижня для дати {date}: {get_day_of_week(date)}")
