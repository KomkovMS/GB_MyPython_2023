"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' -
набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

word_development = 'разработка'
word_socket = 'сокет'
word_decorator = 'декоратор'

def f_print(a, b, c):
    return print(f'{type(a)}, {a}\n'
                 f'{type(b)}, {b}\n'
                 f'{type(c)}, {c}')

def to_unicode_escape(word):
    return word.encode('unicode_escape').decode()

f_print(word_development, word_socket, word_decorator)

word_development_unicode = to_unicode_escape(word_development)
word_socket_unicode = to_unicode_escape(word_socket)
word_decorator_unicode = to_unicode_escape(word_decorator)

f_print(word_development_unicode, word_socket_unicode, word_decorator_unicode)



