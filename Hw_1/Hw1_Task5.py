"""
ДОПОЛНИТЕЛЬНЫЕ:
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

# вариант 1
user_number = int(input('Введите трехзначное число: '))

hundreds = int(user_number / 100 % 10)
tens = int(user_number / 10 % 10)
units = int(user_number % 10)

total = hundreds + tens + units

print(f'{user_number} -> {total}')

# вариант 2
total = 0
my_number = input('Введите трехзначное число: ')

for el in my_number:
    total += int(el)

print(f'{my_number} -> {total}')

