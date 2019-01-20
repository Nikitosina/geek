# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(A1, A2, A3, A4):
    y = A2[0] - A1[0]
    line1 = (-(A1[1] - A2[1]) / y, -(A1[0] * A2[1] - A1[1] * A2[0]))
    y = A3[0] - A2[0]
    line2 = (-(A2[1] - A3[1]) / y, -(A2[0] * A3[1] - A2[1] * A3[0]))
    y = A4[0] - A3[0]
    line3 = (-(A3[1] - A4[1]) / y, -(A3[0] * A4[1] - A3[1] * A4[0]))
    y = A1[0] - A4[0]
    line4 = (-(A1[1] - A4[1]) / y, -(A1[0] * A4[1] - A1[1] * A4[0]))
    if line1[0] == line3[0] and line2[0] == line4[0] and line1[1] != line3[1] and line2[1] != line4[1]:
        return True
    return False


A1 = (1, 1)
A2 = (3, 3)
A3 = (6, 3)
A4 = (4, 1)

print(is_parallelogram(A1, A2, A3, A4))
