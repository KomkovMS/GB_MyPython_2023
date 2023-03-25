"""Тип данных: словарь"""

my_dict = dict(key_1='val_1', key_2='val_2')
print(my_dict)  # -> {'key_1': 'val_1', 'key_2': 'val_2'}

my_dict = {(1, 2): 500, 2: 400, "key_3": True, 4: None}

# keys
print(my_dict.keys())  # -> dict_keys(['key_1', 2, 'key_3', 4])

my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}

# values
print(my_dict.values())  # -> dict_values([500, 400, True, None])

my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}

# items
print(my_dict.items())  # -> dict_items([('key_1', 500), (2, 400), ('key_3', True), (4, None)])

my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}

# get
print(my_dict.get(2))  # -> 400
print(my_dict[1])  # -> 400

my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}

# popitem
print(my_dict.popitem())  # -> (4, None)
print(my_dict.popitem())  # -> ('key_3', True)
print(my_dict.popitem())  # -> (2, 400)
print(my_dict.popitem())  # -> ('key_1', 500)

my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}

# setdefault
print(my_dict.setdefault(5))  # -> None
print(my_dict.items())  # -> dict_items([('key_1', 500), (2, 400), ('key_3', True), (4, None), (5, None)])

my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}

# pop
print(my_dict.pop(2))  # -> 400
print(my_dict.items())  # -> dict_items([('key_1', 500), ('key_3', True), (4, None)])

my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}

# update
my_dict.update({8: 8, 9: 9, 10: 10})
print(my_dict.items())  # -> dict_items([('key_1', 500), (2, 400), ('key_3', True), (4, None), (8, 8), (9, 9), (10, 10)])

my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}

# copy
print(my_dict.copy())  # -> {'key_1': 500, 2: 400, 'key_3': True, 4: None}

my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}

# clear
my_dict.clear()
print(my_dict.items())  # -> dict_items([])
