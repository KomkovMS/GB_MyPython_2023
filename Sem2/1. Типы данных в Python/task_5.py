"""Тип данных: список"""

# -> ['о', 'б', 'ы', 'ч', 'н', 'а', 'я', ' ', 'с', 'т', 'р', 'о', 'к', 'а']
print(list('обычная строка'))

result_list = [2, 'text', 456, 45.3, None]

# append
result_list.append("new_el")
print(result_list)  # -> [2, 'text', 456, 45.3, None, 'new_el']

result_list = [2, 'text', 456, 45.3, None]

# extend
result_list.extend([8, 9, 10])
print(result_list)  # -> [2, 'text', 456, 45.3, None, 8, 9, 10]

result_list = [2, 'text', 456, 45.3, None]

# insert
result_list.insert(1, "ins_el")
print(result_list)  # -> [2, 'ins_el', 'text', 456, 45.3, None]

result_list = [2, 'text', 456, 45.3, None, "ins_el"]

# remove
result_list.remove("ins_el")
print(result_list)  # -> [2, 'text', 456, 45.3, None]

result_list = [2, 'text', 456, 45.3, None]

# pop
obj = result_list.pop(1)
print(result_list)  # -> [2, 456, 45.3, None]

result_list = [2, 'text', 456, 45.3, None]

# index
print(result_list.index(None))  # -> 4

result_list = [2, 'text', 456, 45.3, None]

# count
print(result_list.count(2))  # -> 1

result_list = [2, 'text', 456, 45.3, None]

# reverse
result_list.reverse()
print(result_list)  # -> [None, 45.3, 456, 'text', 2]

result_list = [2, 'text', 456, 45.3, None]

# copy
copy_list = result_list.copy()
print(copy_list)  # -> [2, 'text', 456, 45.3, None]

result_list = [2, 'text', 456, 45.3, None]

# clear
result_list.clear()
print(result_list)  # -> []

my_list = [10, 20, 30]
print((40 or 50) in my_list)  # -> False

list_1 = [30, 'string', None, False]
list_2 = [30, 'string', None, False]

print(list_1 is list_2)  # -> False

list_2 = list_1

print(list_1 is list_2)  # -> True
