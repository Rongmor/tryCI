import pytest

from src import code

@pytest.mark.parametrize(
    'num,result',
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24)
    ]
)
def test_factorial(num, result):
    assert code.factorial(num) == result
