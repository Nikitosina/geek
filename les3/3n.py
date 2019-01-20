# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, arr):
    res = []
    for i in arr:
        if func(i):
            res.append(i)
    return res


print(my_filter(lambda x: type(x) == float, [2, 10.5, -10, 8, 2.1, 0, 14]))
