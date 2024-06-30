import pytest
from source.print_promotion import print_promotion

def test_tc1():
    assert print_promotion(500) == "Free ice cream cone = 1"

def test_tc2():
    assert print_promotion(550) == "Free ice cream cone = 1"

def test_tc3():
    assert print_promotion(600) == "Free ice cream cone = 1"

def test_tc4():
    assert print_promotion(699) == "Free ice cream cone = 1"