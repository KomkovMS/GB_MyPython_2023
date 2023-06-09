"""
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

a1 = int(input('Введите первый элемент арифметической прогрессии: '))
d = int(input('Введите разность прогрессии: '))
n = int(input('Введите количество элементов прогрессии: '))

an = [a1 + i * d for i in range(n)]
print(f'Элементы прогрессии: {an}')

"""
Введите первый элемент арифметической прогрессии: 3
Введите разность прогрессии: 5
Введите количество элементов прогрессии: 8
Элементы прогрессии: [3, 8, 13, 18, 23, 28, 33, 38]
"""

# Эталонное решение:
a1 = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a1 + i * d)
