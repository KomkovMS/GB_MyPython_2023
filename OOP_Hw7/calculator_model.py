class CalculatorModel:
    def __init__(self):
        self.history = []

    def perform_operation(self, operation):
        self.history.append(operation)

    def get_history(self):
        return self.history
