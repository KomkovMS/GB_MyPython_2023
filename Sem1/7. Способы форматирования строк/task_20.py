# Форматирование через f-строки
ip = '192.168.1.4'
mask = 10


print(f"ip-params: {ip}, mask: {mask}")

octets = ['10', '1', '1', '1']
mask = 10

print(f"ip-params: {'.'.join(octets)}, mask: {mask}")

oct1, oct2, oct3, oct4 = [10, 1, 1, 1]

print(f'''IP address: {oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}''')
