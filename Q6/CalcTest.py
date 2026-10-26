import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(5, 3)
        self.assertEqual(result, 15)

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(5,2)
        self.assertEqual(result,2.5)

    def test_modulo_positive_operands(self):
        calc = Calculator()
        result = calc.modulo(5, 3)
        self.assertEqual(result, 2)

    def test_modulo_negative_dividend(self):
        calc = Calculator()
        result = calc.modulo(-5, 3)
        self.assertEqual(result, 1)

    def test_modulo_zero_divisor(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.modulo(5, 0)

    def test_power_positive_exponent(self):
        calc = Calculator()
        result = calc.power(2, 3)
        self.assertEqual(result, 8)

    def test_power_zero_base_zero_exponent(self):
        calc = Calculator()
        result = calc.power(0, 0)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
