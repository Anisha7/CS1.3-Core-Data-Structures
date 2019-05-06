from treemap import TreeMap, TreeNode
import unittest

class TreeNodeTest(unittest.TestCase):
    def test_init(self):
        node = TreeNode(30, "apple")
        assert node.key == 30
        assert node.value == "apple"
        assert node.left is None
        assert node.right is None

    def test_is_leaf(self):
        # Create node with no children
        node = TreeNode(2, "go")
        assert node.is_leaf() is True
        # Attach left child node
        node.left = TreeNode(1, "ap")
        assert node.is_leaf() is False
        # Attach right child node
        node.right = TreeNode(3, "oh")
        assert node.is_leaf() is False
        # Detach left child node
        node.left = None
        assert node.is_leaf() is False
        # Detach right child node
        node.right = None
        assert node.is_leaf() is True

    def test_is_branch(self):
        # Create node with no children
        node = TreeNode(2, "ay")
        assert node.is_branch() is False
        # Attach left child node
        node.left = TreeNode(1, "yo")
        assert node.is_branch() is True
        # Attach right child node
        node.right = TreeNode(3, "boo")
        assert node.is_branch() is True
        # Detach left child node
        node.left = None
        assert node.is_branch() is True
        # Detach right child node
        node.right = None
        assert node.is_branch() is False

    def test_height(self):
        # Create node with no children
        node = TreeNode(4, "woofo")
        assert node.height() == 0
        # Attach left child node
        node.left = TreeNode(2, "hefjwe")
        assert node.height() == 1
        # Attach right child node
        node.right = TreeNode(6, "yolo")
        assert node.height() == 1
        # Attach left-left grandchild node
        node.left.left = TreeNode(1, "gobble")
        assert node.height() == 2
        # Attach right-right grandchild node
        node.right.right = TreeNode(8, "haf")
        assert node.height() == 2
        # Attach right-right-left great-grandchild node
        node.right.right.left = TreeNode(7, "yayay")
        assert node.height() == 3


class TreeMapTest(unittest.TestCase):
    def test_init(self):
        tree = TreeMap()
        assert tree.root is None
        assert tree.size == 0
        assert tree.is_empty() is True

    def test_init_with_list_of_tuples(self):
        tree = TreeMap([(2, 'B'), (1, 'A'), (3, 'C')])
        assert (tree.root.key, tree.root.value) == (2, 'B')
        assert (tree.root.left.key, tree.root.left.value) == (1, 'A')
        assert (tree.root.right.key, tree.root.right.value )== (3, 'C')
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_size(self):
        tree = TreeMap()
        assert tree.size == 0
        tree.set('B')
        assert tree.size == 1
        tree.set('A')
        assert tree.size == 2
        tree.set('C')
        assert tree.size == 3

    def test_keys(self):
        tree = TreeMap([(2, 'B'), (1, 'A'), (3, 'C')])
        assert tree.keys() == [1,2,3]

        tree = TreeMap([('B', 2), ('A', 1), ('C', 3)])
        assert tree.keys() == ['A', 'B', 'C']
        

    def test_values(self):
        tree = TreeMap([(2, 'B'), (1, 'A'), (3, 'C')])
        assert tree.values() == ['A', 'B', 'C']

        tree = TreeMap([('B', 2), ('A', 1), ('C', 3)])
        assert tree.values() == [1,2,3]

    def test_items(self):
        tree = TreeMap([(2, 'B'), (1, 'A'), (3, 'C')])
        assert tree.items() == [(1, 'A'), (2, 'B'), (3, 'C')]

    def test_contains(self):
        tree = TreeMap([(2, 'B'), (1, 'A'), (3, 'C')])
        assert tree.contains(2)
        assert tree.contains(1)
        assert tree.contains(3)

    def test_get(self):
        tree = TreeMap([(2, 'B'), (1, 'A'), (3, 'C')])
        assert tree.get(2) == 'B'
        assert tree.get(1) == 'A'
        assert tree.get(3) == 'C'

    def test_set(self):
        tree = TreeMap()
        tree.set(2, 'B')
        assert tree.contains(2)
        assert tree.get(2) == 'B'
        tree.set(1, 'A')
        assert tree.contains(1)
        assert tree.get(1) == 'A'
        tree.set(3, 'C')
        assert tree.contains(3)
        assert tree.get(3) == 'C'
        
    def test_delete(self):
        tree = TreeMap([(2, 'B'), (1, 'A'), (3, 'C')])
        tree.delete(2)
        assert not tree.contains(2)
        assert tree.contains(1)
        assert tree.contains(3)
        tree.delete(1)
        assert not tree.contains(1)
        assert tree.contains(3)
        tree.delete(3)
        assert tree.is_empty()
        assert not tree.contains(3)