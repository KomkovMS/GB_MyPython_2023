class CalculatorPresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def perform_calculation(self):
        first_number = self.view.get_input_number()
        operator = self.view.get_input_operator()
        second_number = self.view.get_input_number()

        if operator == '+':
            self.model.add(first_number, second_number)
        elif operator == '-':
            self.model.subtract(first_number, second_number)
        elif operator == '*':
            self.model.multiply(first_number, second_number)
        elif operator == '/':
            self.model.divide(first_number, second_number)
        else:
            print("Invalid operator")
            return

        self.view.display_result(self.model.get_result())
