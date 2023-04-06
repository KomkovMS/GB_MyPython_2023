"""Модуль pyyaml_examples"""

import yaml

# считываем данные
with open('data_read.yaml') as f_n:
    F_N_CONTENT = yaml.load(f_n, Loader=yaml.FullLoader)
print(F_N_CONTENT)

# изменяем формат записи
ACTION_LIST = ['msg_1', 'msg_2', 'msg_3']
TO_LIST = ['account_1', 'account_2', 'account_3']
DATA_TO_YAML = {'action': ACTION_LIST, 'to': TO_LIST}

with open('data_write.yaml', 'w') as f_n:
    yaml.dump(DATA_TO_YAML, f_n)

with open('data_write.yaml') as f_n:
    print(f_n.read())
