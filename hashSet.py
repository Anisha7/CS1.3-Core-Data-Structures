from __future__ import division
#!python

"""
HashSet stores values for a set with a hashtable implementation.
"""

from linkedlist import LinkedList

class HashSet(object):
    
    def __init__(self, init_size=8, items = None):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries
        # Insert each key-value entry into the list of buckets,
        # which will rehash them into a new bucket index based on the new size
        if items is not None: 
            for key in items:
                self.set(key)

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}'.format(key) for key in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashSet({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: O(1) always"""
        # Calculate load factor
        # return self.size//len(self.buckets)
        # return float:
        return self.size/len(self.buckets)

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
        Best and worst case running time: O(b) always where b is the number of 
        buckets in hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Best and worst case running time: O(1) always"""
        # return number of key-value entries in each of the buckets
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Best case running time: O(1) if its the first element in the bucket
        Worst case running time: O(m), m = # items in bucket, if its the last element in the bucket"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_v: key_v == key)
        return entry is not None  # True or False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: O(1) if its the first element in the bucket
        Worst case running time: O(m), m = # of items in bucket, if its the last element in the bucket"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_v: key_v == key)
        if entry is not None:  # Found
            # Return the value
            return entry
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key):
        """Insert or update the given key with its associated value.
        Best case running time: O(1) if its the first element in the bucket
        Worst case running time: O(m), m = # of items in bucket, if its the last element in the bucket 
        or does not exist"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_v: key_v == key)
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(entry)
            self.size -= 1
        # Insert the new key-value entry into the bucket in either case
        bucket.append(key)
        self.size += 1 # update size
        # Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:
            # If so, automatically resize to reduce the load factor
            self._resize()

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time: O(1) if its the first element in the bucket
        Worst case running time: O(m), m = # of items in bucket, if its the last element in the bucket 
        or does not exist"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Remove the key-value entry from the bucket
        bucket.delete(key) # (O(m)
        self.size -= 1 # update size

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best and worst case running time: O(N), where N is the number of items, 
        (for both because --> O(N/2) best case if reducing size, O(2N) if increasing size)
        Best and worst case space usage: O(s) where s is the new_size of linkedlist"""
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size
        # Get a list to temporarily hold all current key-value entries
        all_items = self.items() # O(b), b = # of buckets
        # Create a new list of new_size total empty linked list buckets
        # and insert values into new buckets
        self.__init__(new_size, all_items) # O(N), N = # of items in hash table

def test_hash_table():
    ht = HashSet(4)
    print('HashSet: ' + str(ht))

    print('Setting entries:')
    ht.set(1)
    print('set(1): ' + str(ht))
    ht.set(5)
    print('set(5): ' + str(ht))
    print('size: ' + str(ht.size))
    ht.set(10)
    print('set(10): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set(10)
    print('set(10): ' + str(ht))
    ht.set("V")  # Should trigger resize
    print('set(V): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(1): ' + str(ht.get(1)))
    print('get(5): ' + str(ht.get(5)))
    print('get(10): ' + str(ht.get(10)))
    print('get(V): ' + str(ht.get("V")))
    print('contains(5): ' + str(ht.contains(5)))
    print('contains(V): ' + str(ht.contains("V")))

    print('Deleting entries:')
    ht.delete(1)
    print('delete(1): ' + str(ht))
    ht.delete(5)
    print('delete(5): ' + str(ht))
    ht.delete(10)
    print('delete(10): ' + str(ht))
    ht.delete("V")
    print('delete(V): ' + str(ht))
    print('contains(10): ' + str(ht.contains(10)))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()

