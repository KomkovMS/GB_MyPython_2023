"""
Задача 32: Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""


def find_indexes(numbers, min_val, max_val):
    indexes = []
    for index, number in enumerate(numbers):
        if min_val <= number <= max_val:
            indexes.append(str(index))
    return indexes


numbers = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_val = 3
max_val = 7
indexes = find_indexes(numbers, min_val, max_val)
print(' '.join(indexes))  # [1, 2, 3, 6, 7]

# Эталонное решение:
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 3 # int(input())
max_number = 7 # int(input())
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end=' ')
