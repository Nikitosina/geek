# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os

destdir = os.path.abspath('.')

dirname, filename = os.path.split(__file__)
content = open(__file__).read()
open(os.path.join(destdir, filename.split('.')[0] + '_copy.' + filename.split('.')[1]), 'w').write(content)
