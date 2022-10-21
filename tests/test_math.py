"""
This module contains basic unit tests for math operations
Their purpose is to show how to use the pytest framework by example
"""

import pytest


# ---------------------------
# A most basic test function
# ---------------------------
@pytest.mark.math
def test_one_plus_one():
    assert  1+1 == 2

@pytest.mark.math
def test_one_plus_two():
    a=1
    b=2
    c=3
    assert a+b==c

# -------------------------------------------
# Test function that verifies an exception
# -------------------------------------------
@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0

    assert  "division by zero" in str(e.value)

# -------------------------------------------
# A parameterized test function for multiplication
# -------------------------------------------
products =[
    (2,3,6),            # two positive integers
    (1,99,99),          # Identity : multiplying any number by 1
    (0,99,0),           # zero : multiplying any number by 0
    (3,-4,-12),         # positive by a negative
    (-5,-5,25),         # negative by a negative
    (2.5,6.7,16.75)     # multiply floats
]

@pytest.mark.math
@pytest.mark.parametrize('a,b,product',products)
def test_multiplication(a,b,product):
    assert  a*b == product

# DRY Principle : Don't repeat yourself
