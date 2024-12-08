# 8.	Секунди між часами

# Функція, яка рахує, скільки секунд пройшло між двома моментами часу.

from datetime import datetime


def seconds_between_times(time1, time2):
    """
    Рахує кількість секунд між двома моментами часу.

    Параметри:
    time1 (str): Перший момент часу у форматі 'HH:MM:SS'.
    time2 (str): Другий момент часу у форматі 'HH:MM:SS'.

    Повертає:
    int: Кількість секунд між двома моментами часу.
    """
    # Перетворення рядків у об'єкти datetime
    time_format = '%H:%M:%S'
    t1 = datetime.strptime(time1, time_format)
    t2 = datetime.strptime(time2, time_format)

    # Обчислення різниці часу в секундах
    delta = abs((t2 - t1).total_seconds())

    return int(delta)


# Приклад використання:
time1 = '12:30:15'
time2 = '14:45:30'
print(f"Кількість секунд між {time1} і {time2}: {seconds_between_times(time1, time2)} секунд.")