"""Тип данных: кортеж"""

print(tuple('обычная строка'))  # -> ('о', 'б', 'ы', 'ч', 'н', 'а', 'я', ' ', 'с', 'т', 'р', 'о', 'к', 'а')
my_l = [4, 234, 45.8, "text", "word", "el", True, None]
print(my_l.__sizeof__())  # -> 104

my_t = (4, 234, 45.8, "text", "word", "el", True, None)
print(my_t.__sizeof__())  # -> 88
