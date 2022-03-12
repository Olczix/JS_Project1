import math
import pytest
from function import factorial_function


@pytest.mark.parametrize("number", [0, 1, 5, 10])
def test_factorial_function(number):
    assert math.factorial(number) == factorial_function(number)


@pytest.mark.parametrize("number", [-1, 0.3, -1.3, 5.0])
def test_fail_factorial_function(number):
    with pytest.raises(ValueError):
        factorial_function(number)
