"""
Unit tests for the calculator library
"""


import calculator


class TestCalculator:

    """
    Testing code for math functions whose definition in calculator.py
    """

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
