# Гармонічний ряд

# Напишіть функцію, яка обчислює суму перших n членів гармонічного ряду.

def harmonic_sum(n):

    sum_harmonic = 0.0
    for i in range(1, n + 1):
        sum_harmonic += 1 / i

    return sum_harmonic

n = 2
result = harmonic_sum(n)
print(f"Сума перших {n} членів гармонічного ряду: {result:.4f}")
