import math
import mmh3
from bitarray import bitarray

class BloomFilter():
    def __init__(self, items_count, false_positive_probability):
        self.false_positive_probability = false_positive_probability
        self.bit_size = self.get_size(items_count)
        self.hash_count = self.get_hash_count(self.bit_size, items_count)
        self.bit_array = bitarray(self.bit_size)
        #set all array starts as 0
        self.bit_array.setall(0)

    def add(self, item):
        digest = []
        for index in range(self.hash_count):
            mmh3_val = mmh3.hash(item, index) % self.bit_size
            digest.append(mmh3_val)
            self.bit_array[mmh3_val] = True
    
    def check(self, item):
        for index in range(self.hash_count):
            mmh3_val = mmh3.hash(item, index) % self.bit_size
            if not self.bit_array[mmh3_val]:
                return False
        return True

    def get_size(self, items_count):
        items_log = items_count * math.log(self.false_positive_probability)
        pow_log = math.log(2) ** 2
        bit_size_arr = -(items_log) / pow_log
        return int(bit_size_arr)
    
    def get_hash_count(self, bit_size, items_count):
        return int((bit_size/items_count) * math.log(2))
