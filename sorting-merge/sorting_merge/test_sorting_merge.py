import pytest
from sorting_merge.sorting_merge import merge_sort

def test_merge():
    arr = [4,19,45,2,7,50]
    expected = [2,4,7,19,45,50]
    assert merge_sort(arr) == expected

def test_merge_2():
    arr = [10,21,0,16,9,20]
    expected = [0,9,10,16,20,21]
    assert merge_sort(arr) == expected