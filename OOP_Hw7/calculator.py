class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def square_root(self, num):
        import cmath
        return cmath.sqrt(num)

    def power(self, num, exponent):
        return num ** exponent
