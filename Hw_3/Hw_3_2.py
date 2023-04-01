"""
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0

"""


def input_numbers():
    count = 1
    my_list = []
    while count < 3:
        number = float(input(f'Введите {count} число: '))
        my_list.append(number)
        count += 1
    return my_list


def division_numbers(my_lst):
    return my_lst[0] / my_lst[1]


try:
    my_lst = input_numbers()
    result = division_numbers(my_lst)
except ZeroDivisionError:
    print('Вы что? Пытаетесь делить на 0!')
else:
    print(f'результат деления: {result}')

