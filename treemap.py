"""
TreeMap implements a Map/Dictionary that takes in a key, value pair.

Key is hashed to int stored in the tree
"""

from stack import Stack
from queue import Queue

class TreeNode(object):
    
    def __init__(self, key, value=0):
        """Initialize this binary tree node with the given data."""
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r}:{!r})'.format(self.key, self.value)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # Check if both left child and right child have no value
        return self.left == None and self.right == None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # Check if either left child or right child has a value
        return self.left != None or self.right != None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best case running time: log(N) if balanced and worst case running time: 
        O(N) if not balanced, where N = total items"""
        if self.left == None and self.right == None:
            return 0
        left = 0
        right = 0
        if self.left != None:
            left = 1 + self.left.height()
        if self.right != None:
            right = 1 + self.right.height()
        
        return max(left, right)

class TreeMap(object):
    
    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for key, value in items:
                self.set(key, value)

    def is_empty(self):
        return self.root == None or self.size == 0

    def _items_in_order(self, val):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append, val)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit, val):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best case running time: O(logN) if balanced tree
        Worst case running time: O(N) if unbalanced tree"""
        if (node is None):
            return
        # Traverse left subtree, if it exists
        self._traverse_in_order_recursive(node.left, visit, val)
        # Visit this node's data with given function
        if (val == "key"):
            visit(node.key)
        elif (val == "value"):
            visit(node.value)
        # Traverse right subtree, if it exists
        self._traverse_in_order_recursive(node.right, visit, val)

    def keys(self):
        """Returns all the keys in map in order"""
        return self._items_in_order("key")


    def values(self):
        """Returns all the values in map in order"""
        return self._items_in_order("value")

    def items(self):
        """Returns all the key, value pairs in map in order"""
        if self.is_empty():
            return []
        node = self.root
        items = []
        nodes = Stack()
        nodes.push(node)
        
        # add all of the left nodes
        while (node is not None and node.left is not None):
            nodes.push(node.left)
            node = node.left

        # visit left nodes, bottom to up
        while (not nodes.is_empty()):
            node = nodes.pop()
            if (node is not None):
                # add key value pair to items
                items.append((node.key, node.value))
                # if it has any right nodes, add them to the stack
                if (node.right is not None):
                    temp = node.right
                    nodes.push(temp)
                    # add all of its left nodes
                    while (temp.left is not None):
                        nodes.push(temp.left)
                        temp = temp.left

        return items

    def _find_node_recursive(self, key, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case running time: O(logN) balanced tree
        Worst case running time: O(N) not a balanced tree"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        elif node.key == key:
            # Return the found node
            return node
        # Check if the given item is less than the node's data
        elif key < node.key:
            # Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(key, node.left)
        # TODO: Check if the given item is greater than the node's data
        elif key > node.key:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(key, node.right)

    def contains(self, key):
        # Find a node with the given item, if any
        node = self._find_node_recursive(key, self.root)
        # node = self._find_node_iterative(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def get(self, key):
        node = self._find_node_recursive(key, self.root)

        if node is not None:
            return node.value
        
        raise KeyError("Key does not exist {key}".format(key))

    def _find_parent_node_recursive(self, key, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion).
        Best case running time: O(logN) if balanced tree, O(1) if first element
        Worst case running time: O(N) if unbalanced tree"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        # Check if the given item matches the node's data
        if node.key == key:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif node.key > key:
            # Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(key, node.left, node)  # Hint: Remember to update the parent parameter
        # Check if the given item is greater than the node's data
        elif node.key < key:
            # Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(key, node.right, node)  # Hint: Remember to update the parent parameter


    def set(self, key, value=0):
        # Handle the case where the tree is empty
        if self.is_empty():
            # Create a new root node
            self.root = TreeNode(key, value)
            # Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(key, self.root)
        # Check if the given item should be inserted left of parent node
        if parent.key > key:
            # TODO: Create a new node and set the parent's left child
            parent.left = TreeNode(key, value)
        # Check if the given item should be inserted right of parent node
        elif parent.key < key:
            # TODO: Create a new node and set the parent's right child
            parent.right = TreeNode(key, value)
        # Increase the tree size
        self.size += 1

    def _get_successor(self, node):
        '''Returns the element one step to the right and
        as far left as possible.
        Best case running time: O(logN) if balanced tree, O(1) if first element
        Worst case running time: O(N) if unbalanced tree'''
        temp = node.right
        while temp.left is not None:
            temp = temp.left

        return temp
    
    def _get_predecessor(self, node):
        '''Returns the element one step to the left and
        as far right as possible.
        Best case running time: O(logN) if balanced tree, O(1) if first element
        Worst case running time: O(N) if unbalanced tree'''
        temp = node.left
        while temp.right is not None:
            temp = temp.right

        return temp
       

    def _delete_with_successor(self, parent, node, suc):
        # suc could have a right child
        suc_parent = self._find_parent_node_recursive(suc.key, self.root)
        temp = suc.right # if successor has a right child
        

        if (parent is None and node.key == self.root.key): # root node
            # set suc's pointers to point to root's left and right
            if node.key != suc_parent.key:
                suc_parent.left = temp # restore its suc's parent to have suc's child
            suc.left = self.root.left
            if (self.root.right is not suc):
                suc.right = self.root.right
            # new root is the suc
            self.root = suc

        elif (parent.key > node.key): # left
            # replace parent's left to be successor
            if node.key != suc_parent.key:
                suc_parent.left = temp # restore its suc's parent to have suc's child
            suc.left = parent.left
            suc.right = parent.right
            parent.left = suc

        elif (parent.key < node.key): # right
            # replace parent's right to be successor
            if node.key != suc_parent.key:
                suc_parent.left = temp # restore its suc's parent to have suc's child
            suc.left = parent.left
            suc.right = parent.right
            parent.right = suc


    def _delete_with_predecessor(self, parent, node, pre):
        # pre could have a left child
        pre_parent = self._find_parent_node_recursive(pre.key, self.root)
        temp = pre.left # if predecessor has a left child
        pre_parent.right = temp # restore its pre's parent to have pre's child

        if (parent is None and node.key == self.root.key): # root node
            
            # set suc's pointers to point to root's left and right
            pre.left = self.root.left
            pre.right = self.root.right
            # new root is the suc
            self.root = pre
            
        elif (parent.key > node.key): # left
            # replace parent's left to be successor
            pre.left = parent.left
            pre.right = parent.right
            parent.left = pre

        elif (parent.key < node.key): # right
            # replace parent's right to be successor
            pre.left = parent.left
            pre.right = parent.right
            parent.right = pre

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        Best case running time: O(logN) if balanced tree, O(1) if first element
        Worst case running time: O(N) if unbalanced tree"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases

        node = self._find_node_recursive(item, self.root)
        # not found
        if (node is None):
            return
        # find parent of node
        parent = self._find_parent_node_recursive(item, self.root)
        # update size
        self.size -= 1
        # node has no child
        if (node.is_leaf()):
            print(self.root.key, item)
            # root node
            if (self.root.key == item):
                self.root = None
            # not root
            else:
                if (parent.key > item): # left
                    parent.left = None
                elif (parent.key < item): # right
                    parent.right = None
        # node has one child, left
        elif (node.right is None and node.left is not None):
            # root node
            if (self.root.key == item):
                self.root = node.left
            # not root: set parent's pointer to node's child
            else:
                if (parent.key > item): # left
                    parent.left = node.left
                elif (parent.key < item): # right
                    parent.right = node.left

        # node has one child, right
        elif (node.left is None and node.right is not None):
            # root node
            if (self.root.key == item):
                self.root = node.right
            # not root: set parent's pointer to node's child
            else:
                if (parent.key > item): # left
                    parent.left = node.right
                elif (parent.key < item): # right
                    parent.right = node.right

        # node has two children
        elif (node.is_branch()):
        # predecessor and successor, use whichever is not None
            pre = self._get_predecessor(node) # has no right node
            suc = self._get_successor(node) # has no left node
            if (pre is not None and (suc is None or pre.height() > suc.height())):
                self._delete_with_predecessor(parent, node, pre)
            elif (suc is not None):
                self._delete_with_successor(parent, node, suc)
