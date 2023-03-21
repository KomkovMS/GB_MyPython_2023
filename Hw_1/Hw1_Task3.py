"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = int(input('Введите целое положительное число: '))
summ = 0
count = n
result = ''

while count > 0:
    summ += n
    result += str(summ)
    count -= 1

print(f'сумма чисел: {result}')
