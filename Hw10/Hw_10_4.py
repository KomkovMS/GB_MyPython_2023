"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

word_list = ['разработка', 'администрирование', 'protocol', 'standard']

for word in word_list:
    bytes_word = word.encode()
    print(f"из строкового представления в байтовое для '{word}': {bytes_word}")

    decoded_word = bytes_word.decode()
    print(f"обратное преобразование для '{bytes_word}': {decoded_word}\n")
