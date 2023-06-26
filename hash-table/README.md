# Hash Tables
Implement a Hashtable Class with the following methods:

    set
    Arguments: key, value
    Returns: nothing
    This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
    Should a given key already exist, replace its value from the value argument given to this method.
   
    get
    Arguments: key
    Returns: Value associated with that key in the table
   
    has
    Arguments: key
    Returns: Boolean, indicating if the key exists in the table already.
   
    keys
    Returns: Collection of keys
   
    hash
    Arguments: key
    Returns: Index in the collection for that key

<br>

## Whiteboard Process
Not Required

<br>

## Approach & Efficiency
Time: O(1)
Space: O(n)

<br>

## Solution

    class Hashtable:
        def __init__(self, size=100):
            self.size = size
            self.table = [[] for _ in range(self.size)]

        def set(self, key, value):
            index = self.hash(key)
            bucket = self.table[index]
            for i, pair in enumerate(bucket):
                if pair[0] == key:
                    bucket[i] = (key, value)  
                return
            bucket.append((key, value))  
        
        def get(self, key):
            index = self.hash(key)
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
            return None
        
        def has(self, key):
            index = self.hash(key)
            for pair in self.table[index]:
                if pair[0] == key:
                    return True
            return False

        def keys(self):
            keys = []
            for bucket in self.table:
                for pair in bucket:
                    key = pair[0]
                    if key not in keys:
                        keys.append(key)
            return keys

        def hash(self, key):
        
            total = 0
            for char in key:
                total += ord(char)
            return total % self.size