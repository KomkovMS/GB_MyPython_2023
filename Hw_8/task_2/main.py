"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }

    with open('orders.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    data['orders'].append(order)

    with open('orders.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


write_order_to_json('item_1', 1, 1000, 'Sidorov S.S', '24.09.2017')
write_order_to_json('item_2', 2, 2000, 'Komkov K.K.', '11.01.2018')
write_order_to_json('item_3', 3, 3000, 'Ivanov V.V.', '11.01.2018')
write_order_to_json('item_4', 4, 5000, 'Andreev A.A.', '11.01.2018')

write_order_to_json('item_4', 2, 5000, 'Andreev A.A.', '11.01.2018')
