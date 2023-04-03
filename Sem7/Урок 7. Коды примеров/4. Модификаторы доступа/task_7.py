class Auto:
    def __init__(self):
        self.auto_name = "Mazda"
        self._auto_year = 2019
        self.__auto_model = "CX9"


a = Auto()
print(a.auto_name)  # -> Mazda
print(a.auto_model)  # -> AttributeError: 'Auto' object has no attribute 'auto_model'
