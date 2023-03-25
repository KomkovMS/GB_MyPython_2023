"""Тип данных: bytes и bytearray"""
print(b'text')  # -> b'text'
print('текст'.encode('utf-8'))  # -> b'\xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'
print(bytes('text', encoding='utf-8'))  # -> b'text'

print(bytes([10, 20, 30, 40]))  # -> b'\n\x14\x1e('

my_var = bytearray(b"some text")
print(my_var)  # -> bytearray(b'some text')
print(my_var[0])  # -> 115

#my_var[0] = b'h' -> TypeError: an integer is required
my_var[0] = 105
print(my_var)  # -> bytearray(b'iome text')

my_var = bytearray(b"some text")
for i in range(len(my_var)):
    my_var[i] += i

print(my_var)  # -> bytearray(b'spoh$yk\x7f|')
