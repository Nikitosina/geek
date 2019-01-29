# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
    def __init__(self, a, b, c): # tuples
        self.a = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
        self.b = math.sqrt((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2)
        self.c = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        self.p = (self.a + self.b + self.c) / 2

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        return math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))

    def h(self, a):
        return (2 * math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))) / a


t = Triangle((1, 1), (4, 1), (1, 5))
print('a: {}\nb: {}\nc: {}\nP: {}\nS: {}\nh(a): {}'.format(t.a, t.b, t.c, t.perimeter(), t.square(), t.h(t.c)))1
