"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
(X, Y ≤ 1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.

"""

from random import randint as rr

# Вариант 1 (работает не корректно)

# number_pety_x = rr(0, 10)
# number_pety_y = rr(0, 10)
#
# while True:
#     kate_answer_x = int(input('Отгадай первое число: '))
#     kate_answer_y = int(input('Отгадай второе число: '))
#     if ((kate_answer_x == number_pety_x or kate_answer_x == number_pety_y) and
#        (kate_answer_y == number_pety_y or kate_answer_y or number_pety_x)):
#         print('Katy - ты угадала!')
#         break
#     else:
#         s = number_pety_x + number_pety_y
#         p = number_pety_x * number_pety_y
#         print(f'Katy, попробуй заново, подсказка: сумма этих чисел {s},'
#               f'произведение {p}')

# Вариант 2

list_number = []
count = 0

while count < 2:
    list_number.append(rr(0, 10))
    count += 1

print(list_number)

while True:
    kate = input('отгадай два числа, введи их здесь через пробел: ').split()
    for i in range(len(kate)):
        kate[i] = int(kate[i])
    print(kate)
    if kate == list_number or kate == list_number[::-1]:
        print('Katy - ты угадала!')
        break
    else:
        s = sum(list_number)
        p = list_number[0] * list_number[1]
        print(f'Katy, попробуй заново, подсказка: сумма этих чисел {s},'
              f'произведение {p}')
