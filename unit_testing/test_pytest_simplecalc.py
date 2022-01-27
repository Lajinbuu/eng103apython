# Pytest
from unit_testing.simplecalc import SimpleCalc
import pytest

@pytest.fixture
def calc():
    return SimpleCalc()


def test_calc_add(calc):
    calc = SimpleCalc()
    assert calc.add(2, 6) == 8


def test_calc_subtract(calc):
    calc = SimpleCalc()
    assert calc.subtract(4, 7) == -3


def test_calc_multiply(calc):
    calc = SimpleCalc()
    assert calc.multiply(4,6) == 24

def test_calc_divide(calc):
    calc = SimpleCalc()
    assert calc.divide(10, 2) == 5


def test_calc_divide_by_zero_raise_error(calc):
    calc = SimpleCalc()
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)

a = 0.4 * -88.9
print(a)
