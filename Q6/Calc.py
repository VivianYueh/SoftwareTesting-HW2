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
        if b == 0:
            raise ValueError("Modulo divisor must not be zero")
        if b < 0:
            raise NotImplementedError("Negative modulo divisors are not supported yet")
        return a % b
    def power(self, base, exponent):
        if exponent <= 0:
            raise NotImplementedError("Non-positive exponents are not supported yet")
        return base ** exponent
