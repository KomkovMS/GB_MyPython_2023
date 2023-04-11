"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

lst_urls = ['yandex.ru', 'youtube.com']

for el in lst_urls:
    ping_response = subprocess.run(['ping', '-n', '4', el],
                                   capture_output=True)
    encoding = chardet.detect(ping_response.stdout)['encoding']
    print(
        ping_response.stdout.decode(encoding).encode('utf-8').decode('utf-8'))
