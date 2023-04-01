my_tuple = (2, 4, 6)
new_obj = (el+10 for el in my_tuple)

print(new_obj)  # -> <generator object <genexpr> at 0x000001F27498D5C8>

my_tuple = [2, 4, 6]
new_obj = (el+10 for el in my_tuple)

print(new_obj)  # -> <generator object <genexpr> at 0x0000003E13BB9620>
