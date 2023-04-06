"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import re
import csv


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [
        ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for i in range(1, 4):
        filename = f'info_{i}.txt'
        with open(filename) as file:
            data = file.read()

            os_prod = re.compile(r'Изготовитель системы:\s*(\S+)')
            os_name = re.compile(r'Название ОС:\s*(.*)')
            os_code = re.compile(r'Код продукта:\s*(.*)')
            os_type = re.compile(r'Тип системы:\s*(.*)')

            os_prod_list.append(os_prod.findall(data)[0])
            os_name_list.append(os_name.findall(data)[0])
            os_code_list.append(os_code.findall(data)[0])
            os_type_list.append(os_type.findall(data)[0])

            main_data.append(
                [os_prod.findall(data)[0], os_name.findall(data)[0],
                 os_code.findall(data)[0], os_type.findall(data)[0]])
    return main_data


def write_to_csv(csv_file):

    data = get_data()

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


write_to_csv('report.csv')
