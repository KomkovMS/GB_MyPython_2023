"""
Генератор - итерируемый объект, который можно использовать один раз,
т. к. при использовании генератора значения не хранятся в памяти,
а формируются в процессе обращения к ним, по мере запроса.
"""

generator = (param * param for param in range(5))

for el in generator:
    print(el)

"""
0
1
4
9
16
"""

generator = (param * param for param in range(5))

for el in generator:
    print(el)

print(next(generator))

"""
0
1
4
9
16
Traceback (most recent call last):
  File "F:/Курсы GeekBrains. 2020/Основы Python. Ростелеком/Урок 4/Урок 4. Коды примеров/4. Генераторы/task_11.py", line 22, in <module>
    print(next(generator))
StopIteration
"""
