""" Модуль csv_write """

import csv

DATA = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]

#---------------------------------------------------------------------#
# простая запись данных в файл .csv и вывод результата
with open('kp_data_write_1.csv', 'w') as f_n:
    F_N_WRITER = csv.writer(f_n)
    for row in DATA:
        F_N_WRITER.writerow(row)

with open('kp_data_write_1.csv') as f_n:
    print(type(f_n.read()))

#---------------------------------------------------------------------#
with open('kp_data_write_2.csv', 'w') as f_n:
    F_N_WRITER = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
    for row in DATA:
        F_N_WRITER.writerow(row)

with open('kp_data_write_2.csv') as f_n:
    print(f_n.read())

#---------------------------------------------------------------------#
with open('kp_data_write_3.csv', 'w') as f_n:
    F_N_WRITER = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
    F_N_WRITER.writerows(DATA)

with open('kp_data_write_3.csv') as f_n:
    print(f_n.read())

#---------------------------------------------------------------------#
# указания разделителя при чтении
with open('kp_data_delimiter.csv') as f_n:
    F_N_READER = csv.reader(f_n, delimiter='!')
    for row in F_N_READER:
        print(row)

#---------------------------------------------------------------------#
DATA = [{'hostname': 'kp1',
         'location': 'Moscow',
         'model': '2960',
         'vendor': 'Cisco'},
        {'hostname': 'kp2',
         'location': 'Novosibirsk',
         'model': '2960',
         'vendor': 'Cisco'},
        {'hostname': 'kp3',
         'location': 'Kazan',
         'model': '2960',
         'vendor': 'Cisco'},
        {'hostname': 'kp4',
         'location': 'Tomsk',
         'model': '2960',
         'vendor': 'Cisco'}]

with open('kp_data_dictwriter.csv', 'w') as f_n:
    F_N_WRITER = csv.DictWriter(f_n, fieldnames=list(DATA[0].keys()),
                                quoting=csv.QUOTE_NONNUMERIC)
    F_N_WRITER.writeheader()
    for d in DATA:
        F_N_WRITER.writerow(d)

with open('kp_data_dictwriter.csv') as f_n:
    print(f_n.read())
