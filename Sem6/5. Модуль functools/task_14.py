"""
Функция partial()
Позволяет создать новую функцию с частичным указанием передаваемых аргументов.
"""

from functools import partial


def my_func(param_1, param_2):
    return param_1 ** param_2


new_my_func = partial(my_func, 2)
print(new_my_func)  # -> functools.partial(<function my_func at 0x0000012B9FC4BDC8>, 2)
print(new_my_func(4))  # -> 16
