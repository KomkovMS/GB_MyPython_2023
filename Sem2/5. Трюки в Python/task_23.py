"""Сортировка словаря по значениям"""

my_dict = {'python': 1991, 'java': 1995, 'c++': 1983}
print(sorted(my_dict))  # -> ['c++', 'java', 'python']

my_dict = {'python': 1991, 'java': 1995, 'c++': 1983}
print(sorted(my_dict, key=my_dict.get))  # -> ['c++', 'python', 'java']
