import pytest
from insertion.insertion import selection_sort

def test_insertion():
    arr = [4,19,45,2,7]
    expected = [2,4,7,19,45]
    assert selection_sort(arr) == expected

def test_insertion_2():
    arr = [10,21,0,16,9]
    expected = [0,9,10,16,21]
    assert selection_sort(arr) == expected

