# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# [1, 9, 13, 14, 19]

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# from random import randint
# X = -5
# Y = 10
# list_1 = list(randint(X, Y) for i in range(
#     int(input('Введите количество элементов в массиве: '))))
# print(list_1)

max = int(input('Введите максимум: '))
min = int(input('Введите минимум: '))

for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end=' ')