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

    def __iter__(self):
        """This function allows are set to be iterable. Elements can be 
        looped over using 'for item in set'"""
        return self._generator()

    def _generator(self):
        """This function is a helper for iterable. It stores the data we are 
        currently on and gives the next item at each iteration of the loop."""
        for item in self.items():
            yield item
    
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

    def remove(self, item):
        """This function deletes an element from the set but raises an 
        ValueError if not found. The time complexity would be O(m) in the worst 
        case, where m is the number of items in that bucket. The bests case 
        is O(1) and average case is O(1)because we maintain a load factor 
        of 0.75. Space complexity is O(1) because nothing new is being stored."""
        self.delete(item)

    def discard(self, item):
        """This function deletes an element from the set. The time complexity 
        would be O(m) in the worst case, where m is the number of items 
        in that bucket. The bests case is O(1) and average case is O(1)
        because we maintain a load factor of 0.75. Space complexity is
        O(1) because nothing new is being stored."""
        if self.contains(item):
            self.remove(item)

    def pop(self):
        """This function returns and deletes an element from the set. 
        The time complexity would be O(1) always because we just get 
        the first element. Space complexity is O(1) because nothing new 
        is being stored."""
        if self.size == 0:
            raise KeyError('Empty Set')

        for item in self:
            self.remove(item) # O(1) also because deleting first item
            return item

    def clear(self):
        """This function reinitializes an empty set. The time complexity is O(init size)
        and space complexity is also O(init size)."""
        self.__init__()
        # Note: it might be better to delete all elements to save space! 
        # Right now, it reallocates, thus using more space.

    def update(self, t):
        """This function adds all elements from t to our set. 
        The time complexity is O(n) where n is the number of elements in t
        and space complexity is also O(n) because we add that many elements."""
        for item in t:
            self.add(item)

    def intersection_update(self, t):
        """This function updates our set to contain only elements also in t. 
        The time complexity is O(n) where n is the number of elements in our set
        and space complexity is also O(n) because we add that many elements."""
        for item in self:
            if item not in t:
                self.delete(item)
        return self

    def difference_update(self, t):
        """This function updates our set to remove all elements also in t. 
        The time complexity is O(n) where n is the number of elements in our set
        and space complexity is also O(n) because we add that many elements."""
        for item in self:
            if item in t:
                self.delete(item)

    def symmetric_difference_update(self, t):
        """This function updates our set to to have elements from our set and t but not in both. 
        The time complexity is O(n) where n is the number of elements in our set
        and space complexity is also O(n+m) because we add that many elements."""
        items_in_both = self.intersection(t)
        self.update(t) # add all elements from t
        self.difference_update(items_in_both) # remove elements common to s and t

    def issubset(self, t):
        """This function returns true if our entire set is in t. 
        The time complexity is O(n) where n is the number of elements in our set
        and space complexity is also O(n) because we don't allocate new variables."""
        for item in self:
            if item not in t:
                return False
        return True

    def issuperset(self, t):
        """This function returns true if all items in t are in our set. 
        The time complexity is O(n) where n is the number of elements in t
        and space complexity is also O(1) because we don't allocate new variables."""
        for item in t:
            if item not in self:
                return False
        return True

    def union(self, t):
        """This function returns a new set with all elements from our set and t. 
        The time complexity is O(n) where n is max(elements in our set,elements in t)
        and space complexity is also O(n) because we add that many elements."""
        new_set = Set(len(self))
        for item in self:
            new_set.add(item)
        for item in t:
            new_set.add(item)
        return new_set

    def intersection(self, t):
        """This function returns a new set with all elements that are in both our set and t. 
        The time complexity is O(n) where n is the number of elements in our set
        and space complexity is also O(n) because we add that many elements."""
        print("BUT")
        new_set = Set(len(self))
        for item in self:
            if item in t:
                new_set.add(item)

        return new_set

    def difference(self, t):
        """This function returns a new set with all elements that are in our set but not in t. 
        The time complexity is O(n) where n is the number of elements in our set
        and space complexity is also O(n) because we add that many elements."""
        new_set = Set(len(self))
        for item in self:
            if item not in t:
                new_set.add(item)

        return new_set

    def symmetric_difference(self, t):
        """This function returns a new set with elements that are either in our 
        set OR in t, but not both. The time complexity is O(n) where n is the 
        number of elements in our set and space complexity is also O(n) because 
        we add that many elements."""
        new_set = Set(len(self))
        for item in self:
            if item not in t:
                new_set.add(item)

        for item in t:
            if item not in self:
                new_set.add(item)
        return new_set

    def copy(self):
        """This function returns a new set that is a shallow copy of out set. 
        This means that changes made to this set will affect our set as well.
        The time complexity is O(1) and space complexity is also O(1) because 
        we return a 'pointer' to our original set."""
        return self

    