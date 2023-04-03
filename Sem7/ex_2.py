class Item:
    c = 'Китай'

    def __init__(self, *args):
        self.name = args[0]
        self.price = int(args[1])
        self.a = args[2]

    def get_count(self):
        self.price -= 100


obj_1 = Item('Холодильник Самсунг', '500', '20/20/20')

print(obj_1)    # <__main__.Item object at 0x000001D6518EB650>
print(obj_1.c) # Китай
print(obj_1.name)   # Холодильник Самсунг
print(obj_1.price)  # 500


obj_1.c = 'сша'
print(obj_1.c)  # сша