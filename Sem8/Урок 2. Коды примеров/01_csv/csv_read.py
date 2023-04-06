""" Модуль csv_read """

import csv

# Простое чтение из файла kp_data.csv
# Получаем итератор объекта
with open('kp_data.csv') as f_n:
    F_N_READER = csv.reader(f_n)
    print(type(F_N_READER))
    for row in F_N_READER:
        print(row)

# Преобразование итератора в список
with open('kp_data.csv') as f_n:
    F_N_READER = csv.reader(f_n)
    print(list(F_N_READER))

# Разделение строки заголовков от содержимого
with open('kp_data.csv') as f_n:
    F_N_READER = csv.reader(f_n)
    F_N_HEADERS = next(F_N_READER)
    print('Headers: ', F_N_HEADERS)
    for row in F_N_READER:
        print(row)

# Вывод результата с помощью метода DictReader
with open('kp_data.csv') as f_n:
    F_N_READER = csv.DictReader(f_n)
    for row in F_N_READER:
        print(row)
        print(row['hostname'], row['model'])
