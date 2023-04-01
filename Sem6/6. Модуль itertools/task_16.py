"""
Функция cycle()
Это функция, создающая итератор для формирования бесконечного цикла набора значения
"""

from itertools import cycle

с = 0
for el in cycle("ABC"):
    if с > 10:
        break
    print(el)
    с += 1

"""
A
B
C
A
B
C
A
B
C
A
B
"""
