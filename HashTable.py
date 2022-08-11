from LinkedList import LinkedList

class HashTable:
    def __default_hash(self, key) -> int: # default hash
        s = str(key)     # transform the key into a string
        return ord(s[0]) # returns the ascii value of first character

    table_size: int = 7
    table: list[LinkedList] = []
    length: int = 0
    __hash_func = None

    def __init__(self, size: int = 0, hash_function = None):
        if hash_function and hasattr(hash_function, "__call__"):  # validating hash function
            self.__hash_func = hash_function
        else:
            self.__hash_func = self.__default_hash
        
        if size > 0:
            self.table_size = size

        for _ in range(self.table_size):  # creating the array
            self.table.append(LinkedList())


    def hash(self, key):  # key hasher wrapper
        return self.__hash_func(key) % self.table_size  # mod the hash to fit table size


    def put(self, key, value):  # insert or update key, value
        try:
            pair = self._find(key)  # check if key exists
            pair[1] = value          # update the value of pair
        except KeyError:
            bucket = self.table[self.hash(key)]  # finding bucket
            bucket[0] = [key, value]             # setting pair at head of bucket
            self.length += 1                     # update hash table length


    def _find(self, key):  # find a pair
        bucket = self.table[self.hash(key)]  # get the bucket
        for pair in bucket:  # loop through bucket
            if pair[0] == key:  # check if key matches
                return pair  # return the pair
        raise KeyError


    def find(self, key):  # return the value of pair
        return self._find(key)[1]


    def remove(self, key):  # removes a key, value pair
        bucket = self.table[self.hash(key)]  # get the bucket
        for sub_index, pair in enumerate(bucket):  # loop through the bucket
            if pair[0] == key:  # check if key matches
                del bucket[sub_index]  # remove the pair from bucket
                self.length -= 1
                return
        raise KeyError


    def clear(self):  # clear all buckets
        for bucket in self.table:
            bucket.clear()
        self.length = 0


    def size(self):  # returns the number of items in the HashTable
        return self.length


    def print(self):  # print the hash table
        for bucket in self.table:  # for each bucket
            bucket.print()  # print the bucket

    # HELPERS
    def __getitem__(self, key): return self.find(key)
    def __setitem__(self, key, value): self.put(key, value)
    def __delitem__(self, key): self.remove(key)
    def __len__(self): return self.size()


h = HashTable()
h.put("A", 1)
h.put("AA", 2)
h.put("AB", 3)
h.put("BC", 4)
h.put(1, 5)
h.print()
print('len =', len(h))
print()

h['55'] = 5
h[23] = 2194307019
h[0x55] = "HEXA"
h[1] = 'one'
h.print()
print('h[23] =', h[23])
print('len =', len(h))
print()

del h[23]
del h[1]
h.print()
print('len =', len(h))
print()

h.clear()
h.print()
print('len =', len(h))
print()
