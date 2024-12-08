# Завдання на використання функцій з бібліотекою date (середній рівень):

# 1.	Дні між датами

# Напишіть функцію, яка приймає дві дати у форматі YYYY-MM-DD і обчислює кількість днів між ними.

from datetime import datetime

def days_between_dates(date1, date2):
    date1_obj = datetime.strptime(date1, "%Y-%m-%d")
    date2_obj = datetime.strptime(date2, "%Y-%m-%d")

    # Різниця між датами
    delta = abs(date2_obj - date1_obj)
    return delta.days


# Приклад використання
date1 = "2024-12-01"
date2 = "2024-12-08"
days = days_between_dates(date1, date2)
print(f"Кількість днів між {date1} і {date2}: {days}")

