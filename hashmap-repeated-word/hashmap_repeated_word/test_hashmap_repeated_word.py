import pytest
from hashmap_repeated_word.hashmap_repeated_word import repeated_word,most_frequent_words,word_count


def test_repeated_word():
    string = "This is a test. This is only a  test."
    assert repeated_word(string) == "this"

def test_word_count():
    string = "This is a test. This is only a test.this"
    expected_count = {'this': 3, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
    assert word_count(string) == expected_count

def test_most_frequent_words():
    string = "This is a test. This is only a test.this"
    expected_most_frequent = ['this']
    assert most_frequent_words(string) == expected_most_frequent
