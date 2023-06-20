class CalculatorModel:
    def __init__(self):
        self.result = 0

    def add(self, first_number, second_number):
        self.result = first_number + second_number

    def subtract(self, first_number, second_number):
        self.result = first_number - second_number

    def multiply(self, first_number, second_number):
        self.result = first_number * second_number

    def divide(self, first_number, second_number):
        if second_number != 0:
            self.result = first_number / second_number
        else:
            raise ValueError("Cannot divide by zero")

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = result
