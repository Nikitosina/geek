# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    str_number = str(number)
    ind = str_number.find('.')
    res = str_number[:ind + 1]
    str_number = str_number[ind + 1:]
    status = False
    if int(str_number[ndigits + 1]) >= 5:
        status = True
    for i in range(ndigits - 1, -1, -1):
        if status:
            if int(str_number[i]) != 9:
                status = False
                res += str(int(str_number[i]) + 1)
                continue
            else:
                if i == 0:
                    return float(int(res[:ind]) + 1)
                res += '0'
                continue

        res += str_number[i]
    return float(res[:ind + 1] + res[:ind:-1])


print(my_round(21.149999997, 7))
print(my_round(2123.123456788, 6))
print(my_round(2.9999967, 5))
