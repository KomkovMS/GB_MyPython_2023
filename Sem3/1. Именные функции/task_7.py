"""Неопределенное число параметров"""


# неопределенное число позиционных параметров
def my_func(*args):
    return args


print(my_func(10, "text_1", 20, "text_2"))  # -> (10, 'text_1', 20, 'text_2')


# неопределенное число именованных параметров
def my_func(**kwargs):
    return kwargs


print(my_func(el_1=10, el_2=20, el_3="text"))  # -> {'el_1': 10, 'el_2': 20, 'el_3': 'text'}


# имена args и kwargs не являются обязательными
def my_func(**kparams):
   return kparams


print(my_func(el_1=10, el_2=20, el_3="text"))  # -> {'el_1': 10, 'el_2': 20, 'el_3': 'text'}
