import pytest
from hash_table.hash_table import Hashtable

def test_set_and_get():
    hash_table = Hashtable()
    hash_table.set("key1", "value1")
    hash_table.set("key2", "value2")
    assert hash_table.get("key1") == "value1"
    assert hash_table.get("key2") == "value2"

def test_set_overwrite():
    hash_table = Hashtable()
    hash_table.set("key1", "value1")
    hash_table.set("key1", "new_value")
    assert hash_table.get("key1") == "new_value"

def test_get_nonexistent_key():
    hash_table = Hashtable()
    assert hash_table.get("nonexistent_key") is None

def test_keys():
    hash_table = Hashtable()
    hash_table.set("key1", "value1")
    hash_table.set("key2", "value2")
    hash_table.set("key3", "value3")
    keys = hash_table.keys()
    expected_keys = ["key1", "key2", "key3"]
    assert len(keys) == len(expected_keys)
    assert set(keys) == set(expected_keys)

def test_collision_handling():
    hash_table = Hashtable()
    hash_table.set("key1", "value1")
    hash_table.set("key11", "value11")  
    assert hash_table.get("key1") == "value1"
    assert hash_table.get("key11") == "value11"

def test_hash_function():
    hash_table = Hashtable()
    key = "test"
    index = hash_table.hash(key)
    assert 0 <= index < hash_table.size