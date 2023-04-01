"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
к заданному числу X.

Пользователь в первой строке вводит натуральное число N – количество элементов
в массиве.

В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

from random import randint as RI

n = int(input('Введите натуральное число (количество элементов в массиве) N '
              '= '))
x = int(input('Введите число для поиска x = '))

my_list = [RI(1, 10) for i in range(1, n + 1)]
print(my_list)


def func_closest(number, lst):
    if number in lst:
        return number
    else:
        return min(lst, key=lambda y: abs(y - number))


closest = func_closest(x, my_list)
print(closest)
