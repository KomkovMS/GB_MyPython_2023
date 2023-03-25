"""Обмен значениями через кортежи"""

var_1, var_2 = 20, 30
print(var_1, var_2)  # -> 20 30
var_1, var_2 = var_2, var_1
print(var_1, var_2)  # -> 30 20
