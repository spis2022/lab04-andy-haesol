import pytest

from main import rec_product

def test1():
    assert rec_product(0, 5) == 0

def test2():
    assert rec_product(1, 5) == 5

def test3():
    assert rec_product(-1, 5) == -5

def testbisnegative1():
    assert rec_product(5,-1) == -5

def testbisnegative2():
    assert rec_product(-5,-1) == 5