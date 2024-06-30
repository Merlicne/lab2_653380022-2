import pytest
from source.print_promotion import print_promotion

def test_tc1():
    assert print_promotion(1200) == "Free ice cream cone = 1 and chocolate cake = 1"

def test_tc2():
    assert print_promotion(1699) == "Free ice cream cone = 1 and chocolate cake = 1"

def test_tc3():
    assert print_promotion(2400) == "Free ice cream cone = 2 and chocolate cake = 2"

def test_tc4():
    assert print_promotion(2899) == "Free ice cream cone = 2 and chocolate cake = 2"