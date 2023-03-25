"""Тип данных: NoneType"""

print(type(None))  # -> <class 'NoneType'>

my_dict = {'name': 'Ivan', 'surname': 'Ivanov', 'age': 40, 'position': None}
for el in my_dict:
    if my_dict[el] == None:
        print(f"Для сотрудника пока не определен параметр: {el}")

# Для сотрудника пока не определен параметр: position
