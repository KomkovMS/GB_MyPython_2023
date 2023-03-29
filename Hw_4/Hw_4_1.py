"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются
в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""

n = int(input('Введите кол-во элементов первого множества n = '))
m = int(input('Введите кол-во элементов второго множества m = '))

while True:
    my_lst_1 = input(
        f'Введите целые числа первого множества через пробел ({n} символов): '
        f'').split()
    my_lst_2 = input(
        f'Введите целые числа второго множества через пробел ({m} символов): '
        f'').split()
    if n == len(my_lst_1) and m == len(my_lst_2):
        break
    else:
        if n > len(my_lst_1) or m > len(my_lst_1):
            print('Ты ввел меньше, чем нужно')
        else:
            print('Ты ввел больше, чем нужно')


def int_list(lst):
    return [int(x) for x in lst]


my_lst_1, my_lst_2 = int_list(my_lst_1), int_list(my_lst_2)

my_lst_res = []

for n in my_lst_1:
    for m in my_lst_2:
        if n == m:
            my_lst_res.append(n)

my_lst_res = sorted(set(my_lst_res))

print(my_lst_res)

# Эталонное решение:

mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]

set_1 = set()
set_2 = set()

list_1 = list()

a = [int(x) for x in input().split()]
k = set(a)

for i in k:
    set_1.add(i)

b = [int(x) for x in input().split()]
k1 = set(b)

for i in k1:
    set_2.add(i)

lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')
