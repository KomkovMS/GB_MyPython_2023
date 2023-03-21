# Форматирование через метод format()
print('{}'.format(['el_1', 'el_2', 'el_3', 'el_4']))

print("{:>20} {:>20} {:>20}".format('my_param_1', 'my_param_2', 'my_param_3'))

print("{:.3f}".format(5.0/3))

print('Третий элемент: {2}; Второй элемент: {1}; Первый элемент: {0}'.format('el_1', 'el_2', 'el_3'))
