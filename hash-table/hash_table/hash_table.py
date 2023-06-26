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