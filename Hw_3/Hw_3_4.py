"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()

"""


# 1) используя функцию sort()

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    result = sum(my_list[:2])  # my_list[0] + my_list[1]
    return result


print(my_func(107, 14, 213))


# 2) без функции sort()

def my_func_2(a, b, c):
    if a >= b and a >= c:
        result = a + max(b, c)
    elif b >= a and b >= c:
        result = b + max(a, c)
    else:
        result = c + max(a, b)
    return result


print(my_func_2(7, 14, 213))

