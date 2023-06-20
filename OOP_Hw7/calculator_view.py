class CalculatorView:
    def get_input(self):
        num1 = complex(input("Введите первое комплексное число (в формате a+bj): "))
        operator = input("Введите оператор (+, -, *, /, sqrt, pow): ")
        if operator == "sqrt":
            return num1, operator, None
        elif operator == "pow":
            exponent = float(input("Введите степень: "))
            return num1, operator, exponent
        else:
            num2 = complex(input("Введите второе комплексное число (в формате a+bj): "))
            return num1, operator, num2

    def display_result(self, result):
        print(f"Результат: {result}")

    def display_history(self, history):
        print("История операций:")
        for operation in history:
            print(operation)
