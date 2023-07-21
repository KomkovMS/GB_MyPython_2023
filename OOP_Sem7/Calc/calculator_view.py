class CalculatorView:
    def __init__(self):
        pass

    def get_input_number(self):
        input_value = input("Enter a number: ")
        return float(input_value)

    def get_input_operator(self):
        input_value = input("Enter an operator (+, -, *, /): ")
        return input_value[0]

    def display_result(self, result):
        print("Result: " + str(result))
