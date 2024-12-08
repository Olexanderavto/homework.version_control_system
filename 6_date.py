# 6.	День народження

# Функція, яка обчислює, скільки днів залишилося до наступного дня народження.

from datetime import datetime, timedelta


def days_until_birthday(birthday):
    """
    Обчислює кількість днів до наступного дня народження.

    Параметри:
    birthday (str): Дата народження у форматі 'DD-MM-YYYY'

    Повертає:
    int: Кількість днів до наступного дня народження.
    """
    # Поточна дата
    today = datetime.today()

    # Перетворення дати народження на об'єкт datetime
    birthday_date = datetime.strptime(birthday, '%d-%m-%Y')

    # Визначаємо день народження цього року
    this_year_birthday = birthday_date.replace(year=today.year)

    # Якщо день народження вже був цього року, беремо наступний рік
    if today > this_year_birthday:
        this_year_birthday = this_year_birthday.replace(year=today.year + 1)

    # Обчислюємо різницю в днях
    days_left = (this_year_birthday - today).days

    return days_left


# Приклад використання:
birthday = '12-01-1987'  # замініть на вашу дату народження
print(f"До наступного дня народження залишилось {days_until_birthday(birthday)} днів.")
