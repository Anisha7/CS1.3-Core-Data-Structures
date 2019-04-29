#!python
from deque import Deque

class CircularBuffer(object):
    def __init__(self, size, items=[]):
        self.data = Deque()
        self.maxsize = size
        self.size = 0
        for item in items:
            self.enqueue(item)
        assert len(self) <= self.maxsize

    # gets the length of data, always maxsize
    def __len__(self):
        return self.data.length()

    def enqueue(self, item):
        if self.size == self.maxsize:
            # pop item from front
            self.data.pop_front()
            self.size -= 1
        # add item to end
        self.data.push_back(item)
        self.size += 1
        assert len(self) <= self.maxsize

    def dequeue(self):
        if (self.size == 0):
            return None
        item = self.data.pop_front() # get oldest item, from front
        self.size -= 1
        assert len(self) <= self.maxsize
        return item