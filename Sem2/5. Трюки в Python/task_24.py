"""Нумерованные списки"""

for ind, el in enumerate(['a', 'b', 'c', 'd']):
    print(ind, el)

'''
0 ноль
1 один
2 два
3 три
'''

for ind, el in enumerate(['один', 'два', 'три'], 2):
    print(ind, el)

'''
1 один
2 два
3 три
'''
