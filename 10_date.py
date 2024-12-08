# 10.	Перевірка дати на правильність

# Реалізуйте функцію, яка перевіряє, чи є заданий рядок правильною датою у форматі YYYY-MM-DD.

from datetime import datetime

def is_valid_date(date_string):
    try:
        # Пробуємо перетворити рядок в дату за форматом YYYY-MM-DD
        datetime.strptime(date_string, "%Y-%m-%d")
        return True  # Якщо перетворення вдалося, дата правильна
    except ValueError:
        return False  # Якщо виникла помилка, дата неправильна

# Приклад використання:
date1 = "2024-12-08"
date2 = "2024-02-31"  # Невірна дата

print(is_valid_date(date1))  # Виведе: True
print(is_valid_date(date2))  # Виведе: False
