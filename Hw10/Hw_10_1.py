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

print(type(word_development), word_development)  # <class 'str'> разработка
print(type(word_socket), word_socket)
print(type(word_decorator), word_decorator)

word_development_unicode = ''.join(
    [f'\\u{ord(symbol):04x}' for symbol in word_development])
word_socket_unicode = ''.join(
    [f'\\u{ord(symbol):04x}' for symbol in word_socket])
word_decorator_unicode = ''.join(
    [f'\\u{ord(symbol):04x}' for symbol in word_decorator])

print(type(word_development_unicode),
      word_development_unicode)
# <class 'str'> \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430
print(type(word_socket_unicode),
      word_socket_unicode)
print(type(word_decorator_unicode),
      word_decorator_unicode)

print(type(word_development_unicode))   # <class 'str'>
print(type(word_socket_unicode))
print(type(word_decorator_unicode))