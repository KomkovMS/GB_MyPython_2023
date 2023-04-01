"""
Задача 32: Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""


def find_indexes(numbers, min_val, max_val):
    indexes = []
    for index, number in enumerate(numbers):
        if min_val <= number <= max_val:
            indexes.append(index)
    return indexes


numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8]
min_val = 3
max_val = 7
indexes = find_indexes(numbers, min_val, max_val)
print(indexes)  # [1, 2, 3, 6, 7]

