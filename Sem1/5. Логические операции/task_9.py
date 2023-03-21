# Больше
print(40 > 40) # -> False

# Меньше
print(3 < 9) # -> True

# Равно
print(10 == 10) # -> True

# Не равно
print(2 != 2) # -> False

# Больше или равно
print(40 >= 1) # -> True

# Меньше или равно
print(3 <= 1) # -> False

# Логическое «И». Возвращает значение Истина, если оба операнда имеют значение Истина
print(True and True) # -> True
print(True and False) # -> False
print(False and True) # -> False
print(False and False) # -> False

# Логическое «ИЛИ». Возвращает значение Истина, если хотя бы один из операндов имеет значение Истина
print(True or True) # -> True
print(True or False) # -> True
print(False or True) # -> True
print(False or False) # -> False

# Логическое «НЕ». Изменяет логическое значение операнда на противоположное
print(not True)  # -> False
print(not False) # -> True

# Оператор проверки принадлежности. Возвращает значение Истина, если элемент присутствует в последовательности
print(10 in [10, 20, 30]) # -> True

# Оператор проверки тождественности. Возвращает значение Истина, если операнды ссылаются на один объект
x = 3
y = 3
print(x is y) # -> True
