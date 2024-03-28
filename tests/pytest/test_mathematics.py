import pytest
from src.mathematics import Mathematics


@pytest.fixture(scope='module')
def math():
    m = Mathematics()
    yield m


@pytest.mark.parametrize("case,a,b,expected",
                         [
                             ("positive", 2, 2, 4),
                             ("zero", -2, 2, 0),
                             ("negative", -2, -2, -4),
                         ])
def test_sum(math, case, a, b, expected):
    assert math.sum(a, b) == expected


@pytest.mark.parametrize("case,a,b,expected",
                         [
                             ("positive", 4, 2, 2),
                             ("zero", 2, 2, 0),
                             ("negative", 2, 4, -2),
                         ])
def test_subtract(math, case, a, b, expected):
    assert math.subtract(a, b) == expected


@pytest.mark.parametrize("case,a,b,expected",
                         [
                             ("positive", 2, 2, 4),
                             ("zero", 2, 0, 0),
                             ("negative", 2, -2, -4),
                         ])
def test_multiply(math, case, a, b, expected):
    assert math.multiply(a, b) == expected


def test_divide_exception(math):
    with pytest.raises(ZeroDivisionError):
        math.divide(1, 0)


@pytest.mark.parametrize("case,a,b,expected",
                         [
                             ("positive", 2, 2, 1),
                             ("zero", 0, 2, 0),
                             ("negative", -2, 2, -1),
                             ("fraction", 2, 4, 0.5),
                         ])
def test_divide(math, case, a, b, expected):
    assert math.divide(a, b) == expected
