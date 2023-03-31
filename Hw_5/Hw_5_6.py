"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""

# n = 6
# r = n * (n + 1) / 2


# 1
# def func(n, res = 0):
# 	# с помощью цикла
# 	while n > 0:
# 		res += n
# 		n -= 1
# 	return res

# print(f'{func(n)} = {int(r)}')	# 21 = 21


def func_3(n):
    # с помощью рекурсии
    if n == 1:
        return n
    else:
        return n + func_3(n - 1)


def func2(n, res=''):
    # с помощью цикла
    while n > 0:
        res += '+' + str(n)
        n -= 1
    res = res[::-1]
    return res[:-1]


n = 6
right = n * (n + 1) / 2
left = func_3(n)

if right == left:
    print(f'Равенство выполняется:\n'
          f'{left} = {int(right)}\n'
          f'{func2(n)} = {n}({n}+1)/2')
else:
    print(f'Равенство НЕ выполняется')