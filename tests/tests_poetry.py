import pytest


@pytest.mark.parametrize('x,y',[pytest.param(2, 9, id='x: 2, y: 9'),
                                pytest.param(9, 2, id='x: 9, y: 2')])
def test_version(x, y):
    a = x + y
    assert a == 11