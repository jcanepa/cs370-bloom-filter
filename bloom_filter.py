import hashlib

class BloomFilter:
    def __init__(self, size, hash_count):
        """
        Initialize a new BloomFilter object.

        Args:
            size (int): The size of the bit array.
            hash_count (int): The number of hash functions.
        """
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        """
        Make list of hashes for the item.
        """
        hash_list = []
        for i in range(self.hash_count):
            # unique input converted into UTF-8 byte sequence
            item_bytes = (str(item) + str(i)).encode()
            # hexidecimal representation of the MD5 hash object
            hash_hex = hashlib.md5(item_bytes).hexdigest()
            # convert hex hash to integer, mod by size of BloomFilter
            hash_value = int(hash_hex, 16) % self.size
            # append resulting hash value
            hash_list.append(hash_value)
        return hash_list

    def add(self, item):
        """
        Add item to bloom filter.
        """
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def check(self, item):
        """
        Check if item is in bloom filter.
        """
        for hash_value in self._hashes(item):
            if self.bit_array[hash_value] == 0:
                return "no"
        return "maybe"