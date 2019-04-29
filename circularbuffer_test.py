#!python

from circularbuffer import CircularBuffer
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class CircularBufferTest(unittest.TestCase):
    def test_init(self):
        buf = CircularBuffer(5, [0,1,2,3,4])
        assert len(buf) == 5
        buf = CircularBuffer(5, [0,1,2,3,4,5,6,7])
        assert len(buf) == 5
        buf = CircularBuffer(5, [0,1,2])
        assert len(buf) == 3
        buf = CircularBuffer(5, [0,'hi',2,3,4,'why',6,7])
        assert len(buf) == 5

    def test_enqueue(self):
        buf = CircularBuffer(5)
        assert len(buf) == 0
        buf.enqueue('hi')
        assert len(buf) == 1
        buf.enqueue('boo')
        buf.enqueue('yo')
        buf.enqueue(1)
        buf.enqueue(2)
        buf.enqueue(10)
        assert len(buf) == 5

    def test_dequeue(self):
        # initialize a buffer with 5 elements
        buf = CircularBuffer(5, [0,1,2,3,4])
        assert len(buf) == 5
        assert buf.dequeue() == 0
        assert buf.dequeue() == 1
        assert buf.dequeue() == 2
        assert buf.dequeue() == 3
        assert buf.dequeue() == 4
        assert len(buf) == 0

        # initialize a buffer with 5 elements, but add only 2
        buf = CircularBuffer(5, [0,1,2])
        assert len(buf) == 3
        assert buf.dequeue() == 0
        assert buf.dequeue() == 1
        assert buf.dequeue() == 2
        assert buf.dequeue() == None
        assert buf.dequeue() == None
        assert len(buf) == 0

        # initialize a buffer with 5 elements, but add more than 5
        buf = CircularBuffer(5, [0,1,2,3,4,5,6,7])
        assert len(buf) == 5
        assert buf.dequeue() == 3
        assert buf.dequeue() == 4
        assert buf.dequeue() == 5
        assert buf.dequeue() == 6
        assert buf.dequeue() == 7
        assert buf.dequeue() == None
        assert len(buf) == 0
