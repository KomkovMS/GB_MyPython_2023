from calculator_view import CalculatorView
from calculator_model import CalculatorModel
from calculator_presenter import CalculatorPresenter


def main():
    view = CalculatorView()
    model = CalculatorModel()
    presenter = CalculatorPresenter(view, model)
    presenter.perform_calculation()


if __name__ == '__main__':
    main()
