from calculator import Calculator
from calculator_model import CalculatorModel
from calculator_view import CalculatorView
from calculator_presenter import CalculatorPresenter

if __name__ == "__main__":
    calculator = Calculator()
    model = CalculatorModel()
    view = CalculatorView()
    presenter = CalculatorPresenter(model, view, calculator)

    presenter.run()
