import pytest
from source.print_promotion import print_promotion

def test_tc1():
    assert print_promotion(0) == "Thank you and see you next time"

def test_tc2():
    assert print_promotion(150) == "Thank you and see you next time"

def test_tc3():
    assert print_promotion(300) == "Thank you and see you next time"

def test_tc4():
    assert print_promotion(499) == "Thank you and see you next time"