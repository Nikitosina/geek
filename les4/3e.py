# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

data = [9, 8, 15, 2, -5, 31, -12]
new = [i for i in data if i % 3 == 0 and i > 0 and i % 4 != 0]

print(new)
