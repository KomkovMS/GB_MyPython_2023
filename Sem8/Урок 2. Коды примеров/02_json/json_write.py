"""Модуль json_write"""

import json

# преобразование python-объекта (словаря) в строку в формате json
DICT_TO_JSON = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
    }

with open('mes_example_write_1.json', 'w') as f_n:
    f_n.write(json.dumps(DICT_TO_JSON))

with open('mes_example_write_1.json') as f_n:
    print(f_n.read())

# запись python-объекта в файл в формате json
DICT_TO_JSON = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
    }

with open('mes_example_write_2.json', 'w') as f_n:
    json.dump(DICT_TO_JSON, f_n)

with open('mes_example_write_2.json') as f_n:
    print(f_n.read())

# использование дополнительных параметров записи
DICT_TO_JSON = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
    }

with open('mes_example_write_3.json', 'w') as f_n:
    json.dump(DICT_TO_JSON, f_n, sort_keys=True, indent=4)

with open('mes_example_write_3.json') as f_n:
    print(f_n.read())
