"""Тип данных: строка"""

my_str = "простая строка"
print(my_str)  # -> простая строка
print(type(my_str))  # -> <class 'str'>

# конкатенация
s1 = 'abra'
s2 = 'kadabra'
print(s1 + s2)  # -> abrakadabra

# Взятие элемента по индексу
s = 'abrakadabra'
print(s[1])  # -> b

# Извлечение среза
s = 'abrakadabra'
print(s[4:7])  # -> kad
print(s[3:-3])  # -> akada
print(s[:5])  # -> abrak
print(s[3:])  # -> akadabra
print(s[:])  # -> abrakadabra
print(s[::-1])  # -> arbadakarba
print(s[1:7:2])  # -> baa
