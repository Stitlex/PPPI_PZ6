import pytest
from project import add, discount, percent_of

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 5) == 3

def test_percent_of():
    assert percent_of(200, 10) == 20
    assert percent_of(500, 25) == 125

def test_discount():
    assert discount(100, 10) == 90
    assert discount(200, 50) == 100

def test_discount_invalid():
    with pytest.raises(ValueError):
        discount(100, 150)