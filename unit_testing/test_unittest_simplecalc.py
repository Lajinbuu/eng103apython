from simplecalc import SimpleCalc
import unittest

# unit test works
# Class that inherits from TestCase

class CalcTests(unittest.TestCase):

    #calc =SimpleCalc()
    def setUp(self):           # set up runs before every test. Can be used instead of calc = Simplecalc()
        self.calc = SimpleCalc()
        print("Setting up")

    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6
        self.assertEqual(actual, expected)

    def test_subtract(self):
        actual = self.calc.subtract(2, 4)
        expected = -2
        self.assertEqual(actual, expected)

    def test_multiply(self):
        actual = self.calc.multiply(2, 4)
        expected = 8
        self.assertAlmostEqual(actual, expected)


    def test_divide(self):
        actual = self.calc.divide(2, 4)
        expected = 0.5
        self.assertAlmostEqual(actual, expected)


