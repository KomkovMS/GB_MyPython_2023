"""Тип данных: множество"""

perem_1 = set('abrakadabra')
perem_2 = frozenset('abrakadabra')
print(perem_1)  # -> {'r', 'k', 'a', 'd', 'b'}
print(perem_2)  # -> frozenset({'r', 'k', 'a', 'd', 'b'})
perem_1.add('!')
print(perem_1)  # -> {'!', 'r', 'k', 'a', 'd', 'b'}
# perem_2.add('!')
# print(perem_2)  # -> AttributeError: 'frozenset' object has no attribute 'add'

my_set = {400, None, "text", True}
print(my_set)  # -> {400, True, None, 'text'}

my_set = {400, None, "text", True}

# add
my_set.add("another_el")
print(my_set)  # -> {True, 'another_el', 'text', 400, None}

my_set = {400, None, "text", True}

# remove
my_set.remove("text")
print(my_set)  # -> {400, True, None}

my_set = {400, None, "text", True}

# discard
my_set.discard(400)
print(my_set)  # -> {True, 'text', None}

my_set = {400, None, "text", True}

# pop
my_set.pop()
print(my_set)  # -> {True, 'text', None}

my_set = {400, None, "text", True}

# copy
print(my_set.copy())  # -> {400, 'text', None, True}

my_set = {400, None, "text", True}

# clear
my_set.clear()
print(my_set)  # -> set()


lst = [1, 1, 1, 2, 'string', 'string']

print(set(lst))
