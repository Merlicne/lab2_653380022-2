import pytest
from source.print_promotion import print_promotion

def test_tc1():
    try:
        print_promotion(-1)
        assert False
    except:
        assert True

def test_tc2():
    try:
        print_promotion(-10)
        assert False
    except:
        assert True

def test_tc3():
    try:
        print_promotion('one')
        assert False
    except:
        assert True

def test_tc4():
    try:
        print_promotion('1 hundred')
        assert False
    except:
        assert True