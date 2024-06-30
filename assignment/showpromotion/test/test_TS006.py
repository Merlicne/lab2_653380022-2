import pytest
from source.print_promotion import print_promotion

def test_tc1():
    assert print_promotion(1900) == "Free ice cream cone = 1 and chocolate cake = 2"

def test_tc2():
    assert print_promotion(2399) == "Free ice cream cone = 1 and chocolate cake = 2"

def test_tc3():
    assert print_promotion(3100) == "Free ice cream cone = 2 and chocolate cake = 3"

def test_tc4():
    assert print_promotion(3599) == "Free ice cream cone = 2 and chocolate cake = 3"