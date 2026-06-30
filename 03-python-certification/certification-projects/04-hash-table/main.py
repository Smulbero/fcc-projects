class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val        

    def add(self, key, value):
        hash_val = self.hash(key)
        if hash_val not in self.collection:
            self.collection[hash_val] = {}
        self.collection[hash_val][key] = value
       
    def remove(self, key):
        hash_val = self.hash(key)
        if hash_val in self.collection:
            if key in self.collection[hash_val]:
               del self.collection[hash_val][key]
        return

    def lookup(self, key):
        hash_val = self.hash(key)
        if hash_val in self.collection:
            if key in self.collection[hash_val]:            
                return self.collection[hash_val][key]
        return None