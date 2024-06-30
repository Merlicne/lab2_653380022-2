import pytest
from source.print_promotion import print_promotion

def test_tc1():
    assert print_promotion(700) == "Free chocolate cake = 1"

def test_tc2():
    assert print_promotion(900) == "Free chocolate cake = 1"

def test_tc3():
    assert print_promotion(1001) == "Free chocolate cake = 1"

def test_tc4():
    assert print_promotion(1199) == "Free chocolate cake = 1"