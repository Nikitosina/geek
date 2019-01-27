# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os


for dir in list(os.walk('.'))[0][1]:
    print(dir)
