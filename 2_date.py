# 2.	Форматування дати

# Реалізуйте функцію, яка перетворює дату з формату YYYY-MM-DD у формат DD/MM/YYYY.

from datetime import datetime


def format_date(date_str):
    """
    Перетворює дату з формату YYYY-MM-DD у формат DD/MM/YYYY.
    """
    # Перетворення з формату YYYY-MM-DD у об'єкт datetime
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # Форматування у формат DD/MM/YYYY
    formatted_date = date_obj.strftime("%d/%m/%Y")
    return formatted_date


# Приклад використання
date_str = "2024-12-08"
formatted_date = format_date(date_str)
print(f"Форматована дата: {formatted_date}")