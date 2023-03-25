"""О цикле for in для обхода последовательностей"""

"""
for [переменная-итератор] in [последовательность]:
    [действия, выполняемые для каждой переменной]
"""

for el in "my_string":
    print(el)

'''
m
y
_
s
t
r
i
n
g
'''

my_tuple = (1, 2, 3, 4, 5)
my_list = []
for el in my_tuple:
    my_list.append(el * 2)
print(my_list)

'''[2, 4, 6, 8, 10]'''

orig_list = [1, 2, 3, 4, 5]
new_list = []
for el in orig_list:
    new_list.append(el / 2)
print(new_list)

'''[0.5, 1.0, 1.5, 2.0, 2.5]'''

orig_set = {1, 2, 3, 4, 5}
new_set = set()
for el in orig_set:
    new_set.add(el / 2)
print(new_set)

'''{0.5, 1.0, 2.0, 2.5, 1.5}'''

my_dict = {'title': 'Samsung Galaxy', 'price': 20000, 'country': 'China', 'year': '2016'}
for key, value in my_dict.items():
    print(f"{key} - {value}")

'''
title - Samsung Galaxy
price - 20000
country - China
year - 2016
'''
