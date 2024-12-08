# 3.	Наступний понеділок

# Функція, яка обчислює дату наступного понеділка від заданої дати.

from datetime import datetime, timedelta


def next_monday(date_str):
    """
    Обчислює дату наступного понеділка від заданої дати.

    :param date_str: Дата у форматі YYYY-MM-DD
    :return: Дата наступного понеділка у форматі YYYY-MM-DD
    """
    # Перетворення рядка у об'єкт datetime
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # День тижня (понеділок = 0, неділя = 6)
    current_weekday = date_obj.weekday()

    # Дні до наступного понеділка
    days_to_next_monday = (7 - current_weekday) % 7 or 7  # Завжди принаймні 1 день

    # Дата наступного понеділка
    next_monday_date = date_obj + timedelta(days=days_to_next_monday)
    return next_monday_date.strftime("%Y-%m-%d")


# Приклад використання
date_str = "2024-12-08"
next_monday_date = next_monday(date_str)
print(f"Наступний понеділок після {date_str}: {next_monday_date}")
