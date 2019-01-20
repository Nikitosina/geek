# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

import math


def fibonacci(n, m):
    F = (math.sqrt(5) + 1) / 2
    a = int(F ** (n - 1) / math.sqrt(5) + 0.5)
    b = int(F ** n / math.sqrt(5) + 0.5)
    res = [b]
    for i in range(m - n):
        res.append(a + b)
        a, b = b, res[-1]
    return res


print(fibonacci(7, 10))