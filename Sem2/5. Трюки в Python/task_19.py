"""Вывод значения несуществующего ключа в словаре"""

my_dict = {'k_1': 20, 'k_2': True, 'k_3': 'text'}
print(my_dict['k_4'])  # -> KeyError: 'k_4'

my_dict = {'k_1': 20, 'k_2': True, 'k_3': 'text'}
print(my_dict.get('k_4'))  # -> None
