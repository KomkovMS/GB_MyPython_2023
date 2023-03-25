"""Простейшие анонимные функции"""


def named_func(param):
    return param ** 0.5


print(named_func(100))  # -> 10.0

res = lambda param: param ** 0.5
print(res(100))  # -> 10.0
