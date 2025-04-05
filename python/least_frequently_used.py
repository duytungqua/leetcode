"""
Initialize with a cache n size
set(key, value): set key to value 
get(key): get the value of key
"""

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq = {}
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value, freq = self.cache[key]
        self.freq[freq].remove(key)
        if not self.freq[freq]:
            del self.freq[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        self.freq.setdefault(freq + 1, []).append(key)
        self.cache[key] = (value, freq + 1)
        return value