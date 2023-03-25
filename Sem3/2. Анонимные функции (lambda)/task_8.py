"""Простейшие анонимные функции"""


my_func = lambda p_1, p_2: p_1 + p_2
print(my_func(2, 5))  # -> 7
print(my_func("abra", "kadabra"))  # -> abrakadabra

print((lambda p_1, p_2: p_1 + p_2)(2, 5))  # -> 7
print((lambda p_1, p_2: p_1 + p_2)("abra", "kadabra"))  # -> abrakadabra

new_func = lambda *args: sum(args)
print(new_func(10, 20, 30, 40))  # -> (10, 20, 30, 40)
