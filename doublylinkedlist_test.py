#!python

from doublylinkedlist import DoublyLinkedList, BinaryNode
import unittest


class BinaryNodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = BinaryNode(data)
        assert node.data is data
        assert node.next is None
        assert node.prev is None


class LinkedListTest(unittest.TestCase):
    def test_init(self):
        ll = DoublyLinkedList()
        assert ll.head is None
        assert ll.tail is None
        assert ll.size == 0

    def test_init_with_list(self):
        ll = DoublyLinkedList(['A', 'B', 'C'])
        assert ll.head.data == 'A'  # first item
        assert ll.tail.data == 'C'  # last item
        assert ll.head.prev is None # check prev
        assert ll.tail.prev.data == 'B' # check prev
        assert ll.size == 3

    def test_items(self):
        ll = DoublyLinkedList()
        assert ll.items() == []
        ll.append('B')
        assert ll.items() == ['B']
        ll.prepend('A')
        assert ll.items() == ['A', 'B']
        ll.append('C')
        assert ll.items() == ['A', 'B', 'C']

    def test_length(self):
        ll = DoublyLinkedList()
        assert ll.length() == 0
        # append and prepend operations increase length
        ll.append('B')
        assert ll.length() == 1
        ll.prepend('A')
        assert ll.length() == 2
        ll.append('C')
        assert ll.length() == 3
        # delete operations decrease length
        ll.delete('B')
        assert ll.length() == 2
        ll.delete('C')
        assert ll.length() == 1
        ll.delete('A')
        assert ll.length() == 0