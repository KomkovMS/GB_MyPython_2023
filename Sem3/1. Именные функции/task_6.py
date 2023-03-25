"""Аргументы функций: обязательные и необязательные"""


# обязательные параметры
def first_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3


print(first_func(10, 20, 30))  # -> 60


# var_2 и var_3 - необязательные параметры
def second_func(var_1, var_2=20, var_3=30):
    return var_1 + var_2 + var_3


print(second_func(10))  # -> 60
