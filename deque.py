#!python
# -*- coding: utf-8 -*-

from doublylinkedlist import DoublyLinkedList

## ```````````````` Stretch challenge: Deque ````````````````````` ##
# Implement Deque below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class Deque(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = DoublyLinkedList()
        if iterable is not None:
            for item in iterable:
                self.push_back(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return self.list.length()

    def push_front(self, item):
        """ insert item at the front of the deque """
        self.list.prepend(item)

    def push_back(self, item):
        """ insert item at the back of the deque """
        self.list.append(item)

    def front(self):
        """ return the item at the front of the deque """
        if self.is_empty():
            return None
        return self.list.get_at_index(0)

    def back(self):
        """ return the item at the back of the deque """
        if self.is_empty():
            return None
        last_index = self.length()-1
        return self.list.get_at_index(last_index)

    def pop_front(self):
        """  remove and return the item at the front of the deque """
        if self.is_empty():
            raise ValueError("Cannot pop from empty Deque")
        item = self.front()
        self.list.delete(item)
        return item

    def pop_back(self):
        """ remove and return the item at the back of the deque """
        if self.is_empty():
            raise ValueError("Cannot pop from empty Deque")
        item = self.back()
        self.list.delete(item)
        return item