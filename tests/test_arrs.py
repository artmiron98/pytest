from utils import arrs
import  pytest

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], -2, "test") == "test"

def test_get__arrs_zero():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test") == None

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7], -3, -2) == [5]
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7], -8, 2) == [1, 2]

