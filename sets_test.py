#!python

from sets import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class SetTest(unittest.TestCase):
    
    def test_init(self):
        ht = Set(4)
        assert len(ht.buckets) == 4
        assert ht.length() == 0
        assert ht.size == 0

    def test_falsecontains(self):
        ht = Set(4)
        assert len(ht.buckets) == 4
        assert ("apple" in ht) == False
        assert "pie" not in ht
        assert (1 in ht) == False
        assert 3 not in ht

    def test_add(self):
        ht = Set(4, ["apple", "orange", "banana"])
        assert len(ht.buckets) == 4
        assert len(ht) == 3
        ht.add("app")