# Моделювання кидка м'яча

# Створіть функцію, яка моделює траєкторію кидка м'яча, використовуючи формули
# кінематики з урахуванням кута кидка.

import math
import matplotlib.pyplot as plt


def simulate_trajectory(v0, angle, g=9.81, dt=0.01):
    """
    Моделює траєкторію кидка м'яча.

    Параметри:
    v0 (float): Початкова швидкість (м/с).
    angle (float): Кут кидка (градуси).
    g (float): Прискорення вільного падіння (м/с^2), за замовчуванням 9.81.
    dt (float): Крок часу (с), за замовчуванням 0.01.

    Повертає:
    tuple: Списки координат (x, y).
    """
    # Перетворення кута в радіани
    angle_rad = math.radians(angle)

    # Початкові умови
    x, y = 0, 0
    t = 0
    x_coords = []
    y_coords = []

    while y >= 0:  # Поки м'яч у повітрі
        x = v0 * t * math.cos(angle_rad)
        y = v0 * t * math.sin(angle_rad) - 0.5 * g * t ** 2
        if y >= 0:  # Додаємо лише точки над землею
            x_coords.append(x)
            y_coords.append(y)
        t += dt

    return x_coords, y_coords


def plot_trajectory(x, y):
    """
    Будує графік траєкторії.

    Параметри:
    x (list): Координати x.
    y (list): Координати y.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label="Траєкторія м'яча")
    plt.title("Траєкторія кидка м'яча")
    plt.xlabel("Відстань (м)")
    plt.ylabel("Висота (м)")
    plt.grid()
    plt.legend()
    plt.show()


# Приклад використання
v0 = 20  # Початкова швидкість у м/с
angle = 45  # Кут кидка у градусах

x, y = simulate_trajectory(v0, angle)
plot_trajectory(x, y)
