"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

from random import randint


class Card:
    def __init__(self):
        self.numbers = []
        self.s = [0 for _ in range(27)]
        while len(self.numbers) < 15:
            r = randint(1, 90)
            if r not in self.numbers:
                self.numbers.append(r)

        # print(self.numbers)
        i = 0
        while True:
            pos = randint(0, 26)
            if self.s[pos] == 0:
                self.s[pos] = self.numbers[i]
                if i + 1 >= len(self.numbers):
                    break
                i += 1
                continue
        # print(self.s)

    def __str__(self):
        res = ''
        for i in range(len(self.s)):
            if self.s[i] == 0:
                res += '  '
            elif len(str(self.s[i])) == 1:
                res += ' ' + str(self.s[i])
            elif self.s[i] == -1:
                res += ' -'
            else:
                res += str(self.s[i])
            res += ' '
            if i == 8 or i == 17:
                res += '\n'

        return res


class Game:
    def __init__(self):
        self.player = Card()
        self.computer = Card()
        self._status = True
        self.counter = 90
        self.used = []

    def generate_barrel(self):
        while True:
            r = randint(1, 90)
            if r not in self.used:
                self.used.append(r)
                self.counter -= 1
                break

        return self.used[-1]

    def computer_turn(self, barrel):
        try:
            ind = self.computer.s.index(barrel)
            self.computer.s[ind] = -1
        except ValueError:
            pass

    def player_turn(self, ans: bool, barrel):
        if ans:
            try:
                ind = self.player.s.index(barrel)
                self.player.s[ind] = -1
            except ValueError:
                print('В вашей карточки данного бочонка нет, вы проиграли!')
                self._status = False
        else:
            try:
                ind = self.player.s.index(barrel)
                print('В вашей карточке есть этот бочонок, вы проиграли!')
                self._status = False
            except ValueError:
                pass

    def how_many_left(self):
        pl, comp = 0, 0
        for i in range(len(self.player.s)):
            if self.player.s[i] != 0 and self.player.s[i] != -1:
                pl += 1
            if self.computer.s[i] != 0 and self.computer.s[i] != -1:
                comp += 1

        return pl, comp


game = Game()
while game._status:
    barrel = game.generate_barrel()
    print('Новый бочонок: {} (осталось {})'.format(barrel, game.counter))
    print('------ Ваша карточка -----')
    print(game.player)
    print('--------------------------\n-- Карточка компьютера ---')
    game.computer_turn(barrel)
    print(game.computer)
    print('--------------------------')
    p, c = game.how_many_left()
    # print(p, c)
    if p == 0 and c == 0:
        print('Ничья!')
        game._status = False
    elif p == 0:
        print('Вы выиграли!')
        game._status = False
    elif c == 0:
        print('Вы проиграли!')
        game._status = False

    while True:
        inp = input('Зачеркнуть цифру? (y/n)\n')
        if inp == 'y':
            a = True
            break
        elif inp == 'n':
            a = False
            break
        print('Пожалуйста, введите "y" или "n"')

    game.player_turn(a, barrel)
