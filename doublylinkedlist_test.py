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