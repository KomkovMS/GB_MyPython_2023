"""
Оператор yield по назначению схож с оператором return,
но возвращает генератор вместо значения
"""


def generator():
    for el in (10, 20, 30):
        yield el


g = generator()
print(g)

for el in g:
    print(el)


"""
<generator object generator at 0x000001EC0AB5D5C8>
10
20
30
"""
