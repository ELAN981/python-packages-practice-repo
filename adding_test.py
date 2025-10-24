import adding
import pytest

def test_add():
    assert adding.add(2, 3) == 5
    assert adding.add(-1, 1) == 0
    assert adding.add(0, 0) == 0

def test_sub():
    assert adding.sub(5, 3) == 2
    assert adding.sub(0, 0) == 0
    assert adding.sub(-1, -1) == 0

    