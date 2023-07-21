# реализовать метакласс, позволяющий создавать всегда один и тот же объект
# класса (реализовать паттерн синглтон: делигировать метаклассу создание
# нашего нового объекта и записать его в переменную a)

class TypedMeta(type):
    """
    Метакласс, создающий список __slots__,
    который будет содержать только атрибуты типа TypedProperty
    """
    a = None
    def __call__(cls, *args, **kwargs):
        if cls.a is None:
            cls.a = super().__call__(*args, **kwargs)
        return cls.a

class MyClass(metaclass=TypedMeta):
    """Прикладной пользовательский класс"""

    def method_1(self):
        pass

    def method_2(self):
        print("Небольшая проблема")

# синглтон
obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()

print(obj_1 is obj_2 is obj_3)


