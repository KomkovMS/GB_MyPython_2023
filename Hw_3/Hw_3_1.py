"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень

"""


def month_input():
    while True:
        try:
            number = abs(int(input('Введите номер месяца: ')))
            return number
        except:
            print('ОШИБКА! Введите целое число')


msg_list = 'Результат через список:'
msg_dict = 'Результат через словарь:'

# вариант 1 через список

month = month_input()

season = ['зима', 'весна', 'лето', 'осень']

if 0 < month < 13:
    if month == 12 or 0 < month < 3:
        print(f'{msg_list} {season[0]}')
    elif 2 < month < 6:
        print(f'{msg_list} {season[1]}')
    elif 5 < month < 9:
        print(f'{msg_list} {season[2]}')
    else:
        print(f'{msg_list} {season[3]}')
else:
    print('ты что-то не то ввел')

# вариант 2 через словарь:
dict_season = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8],
               'осень': [9, 10, 11]}

month = month_input()

if 0 < month < 13:
    for key, value in dict_season.items():
        for i in value:
            if i == month:
                print(f'{msg_dict} {key}')
else:
    print('ты что-то не то ввел')
