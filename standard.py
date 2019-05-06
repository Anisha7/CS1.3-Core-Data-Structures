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

    def test_size(self):
        ht = Set(4)
        ht.add('a')
        assert ht.size == 1
        ht.add('b')
        assert ht.size == 2
        ht.add('c')
        assert ht.size == 3
        ht.add('d')
        assert ht.size == 4
        # resize triggered
        ht.add('e')
        assert ht.size == 5
        
    def test_contains(self):
        ht = Set(4)
        ht.add('app')
        assert ht.contains('app')
        ht.add(50)
        assert ht.contains(50)
        ht.add("tests tests tests")
        assert ht.contains("tests tests tests")
        ht.add("1 2")
        assert ht.contains("1 2")
        # does not contain
        assert not ht.contains("tests")
        assert not ht.contains("apple")
        assert not ht.contains("pie")
        assert not ht.contains(1)
        assert not ht.contains(100023)
        assert not ht.contains("12")
        assert not ht.contains("")

    def test_add(self):
        # pretty much the same as contains test
        ht = Set()
        ht.add('Apple')
        assert ht.contains('Apple')
        ht.add('wordswordswords')
        assert ht.contains('wordswordswords')
        assert not ht.contains('words')

    def test_remove(self):
        ht = Set(10, ['apple', 'blue', 1, 10, 15, 'yellow', 'cat', 60])
        assert ht.size == 8
        assert ht.contains('apple')
        ht.remove('apple')
        assert ht.size == 7
        assert not ht.contains('apple')
        assert ht.contains('blue')
        ht.remove('blue')
        assert ht.size == 6
        assert not ht.contains('blue')
        assert ht.contains(1)
        ht.remove(1)
        assert not ht.contains(1)
        assert ht.size == 5
        ht.remove(10)
        ht.remove(15)
        ht.remove('yellow')
        ht.remove('cat')
        ht.remove(60)
        assert ht.size == 0

    def test_union(self):
        ht = Set(4, [5, 15, 43])
        t = Set(4, ["apple", "orange", "banana"])
        new_set = ht.union(t)
        assert new_set.contains(5)
        assert new_set.contains("apple")
        assert new_set.contains(15)
        assert new_set.contains(43)
        assert new_set.contains("orange")
        assert new_set.contains("banana")
        assert new_set.size == 6
        # make sure ht and t were not altered
        assert ht.size == 3
        assert t.size == 3

        # test duplicate adding
        ht = Set(4, [5, 15, 43])
        t = Set(4, ["apple", "orange", "banana", 43])
        new_set = ht.union(t)
        assert new_set.size == 6

        # make sure ht and t were not altered
        assert ht.size == 3
        assert t.size == 4

    def test_intersection(self):
        ht = Set(4, [5, 15, 43, "apple"])
        t = Set(4, ["apple", "orange", "banana", 43])
        new_set = ht.intersection(t)
        assert new_set.size == 2
        assert new_set.contains("apple")
        assert new_set.contains(43)
        assert not new_set.contains("orange")
        assert not new_set.contains(15)

        # make sure ht and t were not altered
        assert ht.size == 4
        assert t.size == 4

    def test_difference(self):
        ht = Set(4, [5, 15, 43, "apple"])
        t = Set(4, ["apple", "orange", "banana"])
        new_set = ht.difference(t)
        assert len(new_set) == 3
        assert new_set.contains(5)
        assert new_set.contains(15)
        assert new_set.contains(43)
        assert not new_set.contains("apple")

        # make sure ht and t were not altered
        assert ht.size == 4
        assert t.size == 3

    def test_issubset(self):
        ht = Set(4, ["apple", "orange", "banana", 5, 15, 43, "hey", "yo", "52"])
        t = Set(4, ["apple", "orange", "banana"])
        assert not ht.issubset(t)
        assert t.issubset(ht)
        ht = Set(4, ["apple", "orange", "banana", 5, 15, 43, "hey", "yo", "52"])
        t = Set(4, ["apple", "orange", "banana", "blue"])
        assert not ht.issubset(t)
        assert not t.issubset(ht)