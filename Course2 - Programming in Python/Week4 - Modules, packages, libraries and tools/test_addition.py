import addition
import pytest

def test_add():
    assert addition.add(4, 5) == 9
    assert addition.add(3, 3) == 5


def test_sub():
    assert addition.sub(4, 5) is -1