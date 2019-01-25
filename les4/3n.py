# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
import re

data = [random.randint(0, 9) for _ in range(20)]
res = 0
t = 1

with open('text.txt', 'w', encoding='UTF-8') as f:
    f.write(''.join(list(map(str, data))))

with open('text.txt', 'r', encoding='UTF-8') as f:
    number = f.read()
    print(number)

for i in range(1, len(number) - 1):
    if number[i - 1] == number[i]:
        t += 1
    else:
        if t > res:
            res = t
        t = 1

print(res)
