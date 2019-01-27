import os


def mk_dir(name):
    try:
        os.mkdir('{}'.format(name))
    except FileExistsError:
        print('Папка с таким именем уже существует')
    else:
        print('Успешно создано')


def ch_dir(name):
    try:
        os.chdir(name)
    except FileNotFoundError:
        print('Папки с таким именем не существует')
    else:
        print('Успешно изменена директория')


def walk_dir():
    for dir in list(os.walk('.'))[0][1]:
        print(dir)


def del_dir(name):
    try:
        os.rmdir('{}'.format(name))
    except FileNotFoundError:
        print('Папки с таким именем не существует')
    else:
        print('Успешно удалено')
