import pytest
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series

def test_zero():
    actual=fibonacci(0)
    expected=0
    assert actual == expected

def test_one():
    actual=fibonacci(1)
    expected=1
    assert actual == expected 

def test_two():
    actual=fibonacci(2)
    expected=1
    assert actual == expected  

def test_three():
    actual=fibonacci(3)
    expected = 2
    assert actual == expected

def test_four():
    actual=fibonacci(4)
    expected = 3
    assert actual == expected

def test_five():
    actual=fibonacci(5)
    expected = 5
    assert actual == expected

def test_six():
    actual=fibonacci(6)
    expected = 8
    assert actual == expected

def test_seven():
    actual=fibonacci(7)
    expected = 13
    assert actual == expected

def test_eight():
    actual=fibonacci(8)
    expected = 21
    assert actual == expected

def test_nine():
    actual=fibonacci(9)
    expected = 34
    assert actual == expected


#---------------------------------- Lucas Test --------------------------------

def test_0():
    actual=lucas(0)
    expected = 2
    assert actual == expected

def test_1():
    actual=lucas(1)
    expected = 1
    assert actual == expected

def test_2():
    actual=lucas(2)
    expected = 3
    assert actual == expected

def test_3():
    actual=lucas(3)
    expected = 4
    assert actual == expected

def test_4():
    actual=lucas(4)
    expected = 7
    assert actual == expected

def test_5():
    actual=lucas(5)
    expected = 11
    assert actual == expected

def test_6():
    actual=lucas(6)
    expected = 18
    assert actual == expected

def test_7():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_8():
    actual = lucas(8)
    expected = 47
    assert actual == expected


def test_9():
    actual = lucas(9)
    expected = 76
    assert actual == expected


def test_10():
    actual = lucas(10)
    expected = 123
    assert actual == expected

#---------------------------- Sum test ------------------------------

def test_zero_sum_series():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_one_sum_series():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_two_sum_series():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_three_sum_series():
    actual = sum_series(3)
    expected = 2
    assert actual == expected


def test_four_sum_series():
    actual = sum_series(4)
    expected = 3
    assert actual == expected


def test_five_sum_series():
    actual = sum_series(5)
    expected = 5
    assert actual == expected
def test_six_sum_series():
    actual = sum_series(6)
    expected = 8
    assert actual == expected


def test_seven_sum_series():
    actual = sum_series(7)
    expected = 13
    assert actual == expected


def test_eight_sum_series():
    actual = sum_series(8)
    expected = 21
    assert actual == expected


def test_nine_sum_series():
    actual = sum_series(9)
    expected = 34
    assert actual == expected


def test_ten_sum_series():
    actual = sum_series(10)
    expected = 55
    assert actual == expected