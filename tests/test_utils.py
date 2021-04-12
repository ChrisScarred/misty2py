import pytest

from misty2py.utils import *


@pytest.mark.parametrize("length", [(1), (6), (42)])
def test_random_string(length):
    assert len(get_random_string(length)) == length

@pytest.mark.parametrize("red, green, blue, result", [(0,0,0,{"red": 0, "green": 0, "blue": 0}), (150,50,250,{"red": 150, "green": 50, "blue": 250}), (255,255,255,{"red": 255, "green": 255, "blue": 255})])
def test_rgb_basic(red, green, blue, result):
    assert rgb(red, green, blue) == result

def test_rgb_assert_1():
    with pytest.raises(AssertionError):
        rgb(300, 0, 0)

def test_rgb_assert_2():
    with pytest.raises(AssertionError):
        rgb(-10, 0, 0)

def test_rgb_assert_3():
    with pytest.raises(AssertionError):
        rgb(0, 300, 0)

def test_rgb_assert_4():
    with pytest.raises(AssertionError):
        rgb(0, -10, 0)

def test_rgb_assert_5():
    with pytest.raises(AssertionError):
        rgb(0, 0, 300)

def test_rgb_assert_6():
    with pytest.raises(AssertionError):
        rgb(0, 0, -10)