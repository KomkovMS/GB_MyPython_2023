"""Аргументы функций: позиционные и именованные"""


# позиционные параметры
def first_func(var_2, var_1, var_3):
    return var_1 + var_2 + var_3


print(first_func(10, 20, 30))  # -> 60


# именованные параметры
def second_func(var_3, var_1, var_2):
    print(f"var_2 - {var_2}; var_1 - {var_1}; var_3 - {var_3}")  # -> var_2 - 20; var_1 - 10; var_3 - 30


second_func(var_1=10, var_2=20, var_3=30)
