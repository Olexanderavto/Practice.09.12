#  Число Пі методом Монте-Карло

# Реалізуйте алгоритм для наближеного обчислення числа π\pi методом Монте-Карло.

import random


def calculate_pi(num_points):
    """
    Обчислює наближене значення числа π методом Монте-Карло.

    Параметри:
    num_points (int): Кількість випадкових точок для моделювання.

    Повертає:
    float: Наближене значення числа π.
    """
    points_in_circle = 0

    for _ in range(num_points):
        # Генеруємо випадкові координати (x, y) у межах [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Перевіряємо, чи точка потрапляє всередину кола радіусом 1
        if x ** 2 + y ** 2 <= 1:
            points_in_circle += 1

    # Формула для обчислення π
    return 4 * points_in_circle / num_points


# Приклад використання
num_points = 100000  # Чим більше точок, тим точніше наближення
pi_approximation = calculate_pi(num_points)
print(f"Наближене значення π: {pi_approximation}")
