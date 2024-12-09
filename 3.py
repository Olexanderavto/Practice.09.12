# Кут між двома векторами

# Функція, яка обчислює кут між двома векторами в просторі, використовуючи їх
# скалярний добуток і довжини

import math


def angle_between_vectors(u, v):

    if len(u) != len(v):
        raise ValueError("Вектори повинні мати однакову розмірність.")

    # Скалярний добуток
    dot_product = sum(u_i * v_i for u_i, v_i in zip(u, v))

    # Довжини векторів
    magnitude_u = math.sqrt(sum(u_i ** 2 for u_i in u))
    magnitude_v = math.sqrt(sum(v_i ** 2 for v_i in v))

    if magnitude_u == 0 or magnitude_v == 0:
        raise ValueError("Довжина вектора не може бути нульовою.")

    # Кут у радіанах
    cos_theta = dot_product / (magnitude_u * magnitude_v)

    # Через похибки обчислень cos_theta може вийти за межі [-1, 1]
    cos_theta = max(-1, min(1, cos_theta))

    return math.acos(cos_theta)


# Приклад використання
u = [1, 0, 0]  # Вектор вздовж осі X
v = [0, 1, 0]  # Вектор вздовж осі Y
angle = angle_between_vectors(u, v)

print(f"Кут між векторами: {math.degrees(angle):.2f} градусів")
