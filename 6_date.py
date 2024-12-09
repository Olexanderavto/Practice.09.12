# Завдання на використання функцій з бібліотекою date (високий рівень):


# 1. Обчислення часу в дорозі

# Реалізуйте функцію, яка приймає дату і час початку поїздки та її тривалість (у
# годинах), і обчислює дату й час прибуття.


from datetime import datetime, timedelta

def calculate_arrival(start_date_time, travel_duration_hours):

    start_datetime = datetime.strptime(start_date_time, "%Y-%m-%d %H:%M")

    travel_duration = timedelta(hours=travel_duration_hours)
    arrival_datetime = start_datetime + travel_duration

    return arrival_datetime.strftime("%Y-%m-%d %H:%M")

start_time = "2024-12-09 10:30"
duration = 5.5

arrival_time = calculate_arrival(start_time, duration)
print(f"Час прибуття: {arrival_time}")
