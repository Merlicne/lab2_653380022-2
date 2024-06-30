import pytest
from source.print_promotion import print_promotion

def test_tc1():
    assert print_promotion(1700) == "Free ice cream cone = 2 and chocolate cake = 1"

def test_tc2():
    assert print_promotion(1899) == "Free ice cream cone = 2 and chocolate cake = 1"

def test_tc3():
    assert print_promotion(2900) == "Free ice cream cone = 3 and chocolate cake = 2"

def test_tc4():
    assert print_promotion(3099) == "Free ice cream cone = 3 and chocolate cake = 2"