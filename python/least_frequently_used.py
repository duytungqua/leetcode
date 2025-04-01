"""
Initialize with a cache n size
set(key, value): set key to value 
get(key): get the value of key
"""

class LFUCache:
    def __init__(self, n):
        self.cache = {}
        self.freq = {}
        self.n = n

    def set(self, key, value):
        if len(self.cache) == self.n:
            min_freq = min(self.freq.values())
            for k, v in self.freq.items():
                if v == min_freq:
                    del self.cache[k]
                    del self.freq[k]
                    break
        self.cache[key] = value
        self.freq[key] = 0

    def get(self, key):
        if key in self.cache:
            self.freq[key] += 1
            return self.cache[key]
        
        return -1