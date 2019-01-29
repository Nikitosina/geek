# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math


class Trapeze:
    def __init__(self, a, b, c, d): # tuples
        self.A = a
        self.B = b
        self.C = c
        self.D = d

    def get_sides(self):
        AB = math.sqrt((self.B[0] - self.A[0]) ** 2 + (self.B[1] - self.A[1]) ** 2)
        BC = math.sqrt((self.C[0] - self.B[0]) ** 2 + (self.C[1] - self.B[1]) ** 2)
        CD = math.sqrt((self.D[0] - self.C[0]) ** 2 + (self.D[1] - self.C[1]) ** 2)
        AC = math.sqrt((self.D[0] - self.A[0]) ** 2 + (self.D[1] - self.A[1]) ** 2)
        return AB, BC, CD, AC

    def perimeter(self):
        return sum(self.get_sides())

    def square(self):
        h = abs(self.B[1] - self.A[0])
        return (sum(self.get_sides()[1::2]) / 2) * h

    def is_trapeze(self):
        if self.A[1] == self.D[1] and self.B[1] == self.C[1] and self.get_sides()[0] == self.get_sides()[2]:
            return True
        return False


tr = Trapeze((1, 1), (3, 3), (5, 3), (7, 1))
print('AB: {}\nBC: {}\nCD: {}\nAC: {}\nP: {}\nS: {}\nis_right_trapeze: {}'.format(
    tr.get_sides()[0], tr.get_sides()[1], tr.get_sides()[2], tr.get_sides()[3],
    tr.perimeter(), tr.square(), tr.is_trapeze()))
