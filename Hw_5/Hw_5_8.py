"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""

a = int(input('Введите первое число A = '))
b = int(input('Введите второе число B = '))


# def func(a, b):
#     # при помощи цикла
#     result = a
#     while b > 1:
#         result *= a
#         b -= 1
#     return result


def func2(a, b):
    result = a
    # при помощи рекурсии
    if b == 1:
        return result
    return result * func2(a, b - 1)


# print(f'A = {a}; B = {b} -> {func(a, b)}')
print(f'A = {a}; B = {b} -> {func2(a, b)}')
