# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    ticket = []
    for i in str(ticket_number):
        ticket.append(i)
    if len(ticket) % 2 == 0:
        if sum(list(map(int, ticket[:len(ticket) // 2]))) == sum(list(map(int, ticket[len(ticket) // 2:]))):
            return True
    else:
        if sum(list(map(int, ticket[:len(ticket) // 2]))) == sum(list(map(int, ticket[len(ticket) // 2 + 1:]))):
            return True
    return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

