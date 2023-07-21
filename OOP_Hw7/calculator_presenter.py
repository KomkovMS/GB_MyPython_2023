class CalculatorPresenter:
    def __init__(self, model, view, calculator):
        self.model = model
        self.view = view
        self.calculator = calculator

    def run(self):
        while True:
            num1, operator, num2 = self.view.get_input()

            if operator == "+":
                result = self.calculator.add(num1, num2)
            elif operator == "-":
                result = self.calculator.subtract(num1, num2)
            elif operator == "*":
                result = self.calculator.multiply(num1, num2)
            elif operator == "/":
                if num2 is None:
                    num2 = complex(input(
                        "Введите второе комплексное число (в формате a+bj): "))
                result = self.calculator.divide(num1, num2)
            elif operator == "sqrt":
                result = self.calculator.square_root(num1)
            elif operator == "pow":
                result = self.calculator.power(num1, num2)
            else:
                print("Неверный оператор")
                continue

            self.model.perform_operation(
                f"{num1} {operator} {num2 if num2 is not None else ''}")
            self.view.display_result(result)

            choice = input("Продолжить? (y/n): ")
            if choice.lower() != "y":
                break

        history = self.model.get_history()
        self.view.display_history(history)
