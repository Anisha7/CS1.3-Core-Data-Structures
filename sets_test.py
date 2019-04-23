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

    def test_addremovediscard(self):
        ht = Set(4, ["apple", "orange", "banana"])
        assert len(ht.buckets) == 4
        assert len(ht) == 3
        ht.add("app") # adding strings
        assert len(ht) == 4
        assert ht.contains("app") # contains works
        assert ht.contains("apple")
        assert ht.contains("orange")
        assert ht.contains("banana")
        ht.add(4) # Testing adding numbers
        assert len(ht.buckets) == 8 # resizing works
        assert len(ht) == 5
        assert ht.contains(4)

        # test remove
        ht.remove("apple")
        assert len(ht) == 4
        assert ("apple" not in ht)
        ht.remove("app")
        assert len(ht) == 3
        assert ("app" not in ht)
        with self.assertRaises(ValueError):
            ht.delete('A')  # Key does not exist
        
        # test discard
        ht.discard("app") # does not raise error
        ht.discard("orange")
        assert len(ht) == 2
        assert ("orange" not in ht)

    def test_pop(self):
        ht = Set(4, ["apple", "orange", "banana", 5, 15, 43, "hey", "yo", "52"])
        assert len(ht) == 9
        item = ht.pop()
        assert item not in ht
        assert len(ht) == 8
        item = ht.pop()
        assert item not in ht
        assert len(ht) == 7
        item = ht.pop()
        assert item not in ht
        assert len(ht) == 6
        item = ht.pop()
        assert item is not None
        assert item not in ht
        assert len(ht) == 5

    def test_clear(self):
        ht = Set(4, ["apple", "orange", "banana", 5, 15, 43, "hey", "yo", "52"])
        assert len(ht) == 9
        ht.clear()
        assert len(ht) == 0

    def test_update(self):
        ht = Set(4)
        t = Set(4, ["apple", "orange", "banana", 5, 15, 43, "hey", "yo", "52"])
        ht.update(t)
        assert "apple" in ht
        assert 5 in ht
        assert len(ht) == 9

    def test_intersection_update(self):
        ht = Set(4, ["apple", "orange", "banana", 5, 15, 43, "hey", "yo", "52"])
        t = Set(4, ["apple", "orange", "banana", "blue"])
        ht.intersection_update(t)
        assert "apple" in ht
        assert "orange" in ht
        assert "banana" in ht
        assert 5 not in ht
        assert 15 not in ht
        assert 43 not in ht
        assert "hey" not in ht
        assert "yo" not in ht
        assert "52" not in ht
        assert len(ht) == 3
        assert "blue" not in ht

    def test_difference_update(self):
        ht = Set(4, ["apple", "orange", "banana", 5, 15, 43, "hey", "yo", "52"])
        t = Set(4, ["apple", "orange", "banana", "blue"])
        ht.difference_update(t)
        assert "apple" not in ht
        assert "orange" not in ht
        assert "banana" not in ht
        assert "blue" not in ht
        assert 5 in ht
        assert 15 in ht
        assert 43 in ht
        assert "hey" in ht
        assert "yo" in ht
        assert "52" in ht

    def test_symmetric_difference_update(self):
        ht = Set(4, ["apple", "orange", "banana", 5, 15, 43, "hey", "yo", "52"])
        t = Set(4, ["apple", "orange", "banana", "blue"])
        ht.symmetric_difference_update(t)
        assert "apple" not in ht
        assert "orange" not in ht
        assert "banana" not in ht
        assert "blue" in ht
        assert 5 in ht
        assert 15 in ht
        assert 43 in ht
        assert "hey" in ht
        assert "yo" in ht
        assert "52" in ht

    def test_issubset(self):
        ht = Set(4, ["apple", "orange", "banana", 5, 15, 43, "hey", "yo", "52"])
        t = Set(4, ["apple", "orange", "banana"])
        assert ht.issubset(t) == False
        assert t.issubset(ht)
        ht = Set(4, ["apple", "orange", "banana", 5, 15, 43, "hey", "yo", "52"])
        t = Set(4, ["apple", "orange", "banana", "blue"])
        assert ht.issubset(t) == False
        assert t.issubset(ht) == False

    def test_issuperset(self):
        pass

    def test_union(self):
        pass

    def test_intersection(self):
        pass

    def test_difference(self):
        pass

    def test_symmetric_difference(self):
        pass

    def test_copy(self):
        pass