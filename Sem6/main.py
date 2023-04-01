# перемножим элементы массива на 2
from itertools import count

lst = [1, -2, 3, -4, 5, 6]
result = [el * 2 for el in lst if el > 0]

print(result)

lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

res = []
for el in lst:
    if lst.count(el) == 1:
        res.append(el)

print(res)

res2 = [el for el in lst if lst.count(el) == 1]
print(res2)
