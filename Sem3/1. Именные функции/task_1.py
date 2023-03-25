"""Простейшие именные функции"""


def my_sum(arg_1, arg_2):
    return arg_1 + arg_2


print(my_sum(20, 30))  # -> 50
print(my_sum("abra", "kadabra"))  # -> abrakadabra


def ext_func(var_1):
    def int_func(var_2):
        return var_1 + var_2
    return int_func


f_obj = ext_func(200)  # f_obj - функция
print(f_obj(300))  # -> 500


def my_func():
    pass



print(type(my_func()))  # -> None
