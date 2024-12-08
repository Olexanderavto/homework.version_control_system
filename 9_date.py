# 9.	Дата через X днів

# Напишіть функцію, яка додає задану кількість днів до поточної дати і повертає нову дату.

from datetime import datetime, timedelta


def add_days_to_current_date(days):
    # Отримуємо поточну дату
    current_date = datetime.now()

    # Створюємо об'єкт timedelta з кількістю днів
    new_date = current_date + timedelta(days=days)

    return new_date


# Приклад використання:
days_to_add = 5
new_date = add_days_to_current_date(days_to_add)
print("Нова дата:", new_date.strftime("%Y-%m-%d"))
