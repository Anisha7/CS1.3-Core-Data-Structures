from __future__ import division
#!python
from hashSet import HashSet

class Set(HashSet):
    
    def __init__(self, init_size=8, items = None):
        super().__init__(init_size, items) # initialize variables in parent class

    def __len__(self):
        """This function returns the number of elements in the set.
        It can be used as len(set) in client implementations.
        The complexity of this function is O(1) for time and space.
        This is because the size property is stored in the hash table."""
        return self.size
    
    def __contains__(self, item):
        """This function returns whether or not an element is in the set.
        It can be used as 'item in set' or 'item not in set' in client 
        implementations. The complexity of this function is O(m) for time, 
        where m is the number of elements in the bucket and O(1) for space
        because it is not allocating any new large chunks of space."""
        return self.contains(item)

    def add(self, item):
        """This function adds an element to the set.The time complexity 
        would be O(m) in the worst case, where m is the number of items 
        in that bucket. The bests case is O(1) and average case is O(1)
        because we maintain a load factor of 0.75. Space complexity is
        O(1) because nothing new is being stored."""
        self.set(item)

    # remove x from set s; raises KeyError if not present
    def remove(self, item):
        """This function deletes an element from the set but raises an 
        error if not found. The time complexity would be O(m) in the worst 
        case, where m is the number of items in that bucket. The bests case 
        is O(1) and average case is O(1)because we maintain a load factor 
        of 0.75. Space complexity is O(1) because nothing new is being stored."""
        self.delete(item)

    # removes x from set s if present
    def discard(self, item):
        """This function deletes an element from the set.The time complexity 
        would be O(m) in the worst case, where m is the number of items 
        in that bucket. The bests case is O(1) and average case is O(1)
        because we maintain a load factor of 0.75. Space complexity is
        O(1) because nothing new is being stored."""
        if self.contains(item):
            self.remove(item)

    # remove and return an arbitrary element from s; raises KeyError if empty
    def pop(self):
        pass

    # remove all elements from set s
    def clear(self):
        self.__init__()

    # return set s with elements added from t
    def update(self, t):
        pass

    # return set s keeping only elements also found in t
    def intersection_update(self, t):
        pass

    # return set s after removing elements found in t
    def difference_update(self, t):
        pass

    # return set s with elements from s or t but not both
    def symmetric_difference_update(self, t):
        pass

    # return true if every element in our set is in t
    def issubset(self, t):
        pass

    # return true if every element in t is in our set
    def issuperset(self, t):
        pass

    # return new set with elements from both our set and t
    def union(self, t):
        pass

    # return new set with elements common to our set and t
    def intersection(self, t):
        pass

    # return new set with elements in our set but not in t
    def difference(self, t):
        pass

    # return new set with elements in either our set or t but not both
    def symmetric_difference(self, t):
        pass

    # return new set with a shallow copy of s
    def copy(self, s):
        pass

    