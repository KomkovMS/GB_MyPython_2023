"""Генераторы списков и словарей"""

# генераторное выражение с условием
my_list = [10, 25, 30, 45, 50]
print(my_list)  # -> [10, 25, 30, 45, 50]
new_list = [el for el in my_list if el % 2 == 0]
print(new_list)  # -> [10, 30, 50]

# генераторное выражение с вложенным циклом
str_1 = "abc"
str_2 = "d"
str_3 = "efg"
sets = [i+j+k for i in str_1 for j in str_2 for k in str_3]
print(sets)  # -> ['ade', 'adf', 'adg', 'bde', 'bdf', 'bdg', 'cde', 'cdf', 'cdg']
