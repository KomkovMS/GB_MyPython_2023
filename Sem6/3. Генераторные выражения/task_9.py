"""Модуль random как генератор псевдослучайных чисел"""

# Генерация целых случайных чисел
from random import randint, randrange
print(randint(0, 10))  # -> 4
print(randint(-100, -10))  # -> -25
print(randrange(10))  # -> 5
print(randrange(10, 20))  # -> 14
print(randrange(20, 30, 3))  # -> 29
