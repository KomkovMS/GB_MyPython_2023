"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.

"""

n = int(input('Введите число N = '))
result = 0
count = 0

# 2*0 2*1 2*2 2*3 2*4 2*5 2*6 2*7

while result < n:
    result = 2 * count
    count += 1
    print(f'{result}', end=' ')

# не понял условие, если имеется ввиду так:
# 0**2 1**2 2**2 3**2 4**2 5**2 6**2 7**2
# 0    1    4    9    16   25

print("")

n = int(input('Введите число N = '))
result = 0
count = 0

while result < n:
    result = count ** 2
    count += 1
    if result < n:
        print(f'{result}', end=' ')

# Эталонное решение
print("")

n = int(input('Введите число N = '))
i = 0
while 2 ** i <= n:
    print(2 ** i, end=' ')
    i += 1
