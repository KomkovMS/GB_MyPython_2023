"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

time_input = float(input('Введите время в секундах: '))
time_hours = round(time_input / 3600, 1)
time_minutes = round(time_input / 60, 1)
time_seconds = round(time_input)
time_output = f'{time_hours} : {time_minutes} : {time_seconds}'

print(f'Время в формате ч:м:с - {time_output}')
