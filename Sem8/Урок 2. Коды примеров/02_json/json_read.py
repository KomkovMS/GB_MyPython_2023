"""Модуль json_read"""

import json

# использование метода load для чтения json-файла, как объекта
# преобразуем json-объект в python-объект (словарь)
with open('mes_example_read.json') as f_n:
    OBJ = json.load(f_n)
    print(type(OBJ))

for section, commands in OBJ.items():
    print(section)
    print(commands)

# использование метода loads для чтения json-файла, как строки
# преобразуем json-строку в python-объект (словарь)
with open('mes_example_read.json') as f_n:
    F_N_CONTENT = f_n.read()
    print(F_N_CONTENT)
    print(type(F_N_CONTENT))
    OBJ = json.loads(F_N_CONTENT)
    print(type(OBJ))
    print(OBJ)

for section, commands in OBJ.items():
    print(section)
    print(commands)
