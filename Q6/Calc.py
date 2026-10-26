class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
    def modulo(self, a, b):
        if a < 0 or b < 0:
            raise NotImplementedError("Negative modulo operands are not supported yet")
        return a % b
