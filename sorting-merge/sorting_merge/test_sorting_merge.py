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

def test_merge_3():
    arr = [1,2,8,5,4,6,3]
    expected = [1,2,3,4,5,6,8]
    assert merge_sort(arr) == expected

def test_merge_4():
    arr = [10,20,80,50,40,60,30]
    expected = [10,20,30,40,50,60,80]
    assert merge_sort(arr) == expected