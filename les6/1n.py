# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Pupil:
    def __init__(self, name, surname, patronymic, parents: list):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.parents = parents
        self.cl = None

    def get_parents(self):
        return ', '.join(self.parents)

    def get_full_name(self):
        return self.surname + ' ' + self.name[0] + '.' + self.patronymic[0]

    def get_subjects(self):
        if self.cl:
            res = ''
            for i in range(len(self.cl.teachers)):
                res += '{}. '.format(i + 1) + self.cl.teachers[i].subject + '\n'
            return res
        return 'Ученик не определен в класс'


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject


class Class:
    def __init__(self, name, pupils: list, teachers: list):
        self.name = name
        self.pupils = pupils
        self.teachers = teachers
        for p in pupils:
            p.cl = self

    def get_pupils(self):
        res = ''
        for i in range(len(self.pupils)):
            res += '{}. '.format(i + 1) + self.pupils[i].surname + ' '\
                   + self.pupils[i].name[0] + '.' + self.pupils[i].patronymic[0] + '.\n'

        return res

    def get_teachers(self):
        res = ''
        for i in range(len(self.teachers)):
            res += '{}. '.format(i + 1) + self.teachers[i].name + '\n'

        return res


class School:
    def __init__(self, classes: list):
        self.classes = classes

    def get_classes(self):
        res = ''
        for i in range(len(self.classes)):
            res += '{}. '.format(i + 1) + self.classes[i].name + '\n'

        return res


Ivanov = Pupil('Ivan', 'Ivanov', 'Alexeevich', ['Ann', 'Andrew'])
Petrov = Pupil('Petr', 'Petrov', 'Mikhaylovich', ['Yulya', 'Stepan'])
Trudovic = Teacher('Petrovich', 'Trudi')
MarIvanna = Teacher("Mar'Ivanna", 'Mathematics')
A8 = Class('8 A', [Ivanov, Petrov], [Trudovic, MarIvanna])
sc13 = School([A8])

print('Parents:', Petrov.get_parents(), '\n')
print('Ivanov subjects:')
print(Ivanov.get_subjects())
print('8A class:')
print(A8.get_pupils())
print('Teachers of 8A:')
print(A8.get_teachers())
print('All classes in school 13:')
print(sc13.get_classes())
