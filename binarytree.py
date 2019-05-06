#!python

from stack import Stack
from queue import Queue

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

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


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best case: O(logN) if balanced tree and worst case: O(N) if not balanced"""
        # Check if root node has a value and if so calculate its height
        if self.root == None:
            return 0
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case running time: O(logN) balanced tree?
        Worst case running time: O(N) not a balanced tree?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # node = self._find_node_iterative(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: O(logN) balanced tree
        Worst case running time: O(N) not a balanced tree"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return the node's data if found, or None
        if node is None:
            return None
        return node.data

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case running time: log(N) if balanced and 
        Worst case running time: O(N) if not balanced, 
        where N = total items"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # Create a new root node
            self.root = BinaryTreeNode(item)
            # Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        # parent = self._find_parent_node_iterative(item)
        # Check if the given item should be inserted left of parent node
        if parent.data > item:
            # TODO: Create a new node and set the parent's left child
            parent.left = BinaryTreeNode(item)
        # Check if the given item should be inserted right of parent node
        elif parent.data < item:
            # TODO: Create a new node and set the parent's right child
            parent.right = BinaryTreeNode(item)
        # Increase the tree size
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case running time: O(logN) balanced tree
        Worst case running time: O(N) not a balanced tree"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
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
        elif node.data == item:
            # Return the found node
            return node
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # TODO: Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case running time: O(logN) if balanced tree, O(1) if first element
        Worst case running time: O(N) if unbalanced tree"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the parent of the found node
                return parent
            # TODO: Check if the given item is less than the node's data
            elif node.data > item:
                # TODO: Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif node.data < item:
                # TODO: Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
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
        if node.data == item:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif node.data > item:
            # Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)  # Hint: Remember to update the parent parameter
        # Check if the given item is greater than the node's data
        elif node.data < item:
            # Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)  # Hint: Remember to update the parent parameter

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
        suc_parent = self._find_parent_node_recursive(suc.data, self.root)
        temp = suc.right # if successor has a right child
        

        if (parent is None and node.data == self.root.data): # root node
            # set suc's pointers to point to root's left and right
            if node.data != suc_parent.data:
                suc_parent.left = temp # restore its suc's parent to have suc's child
            suc.left = self.root.left
            if (self.root.right is not suc):
                suc.right = self.root.right
            # new root is the suc
            self.root = suc

        elif (parent.data > node.data): # left
            # replace parent's left to be successor
            if node.data != suc_parent.data:
                suc_parent.left = temp # restore its suc's parent to have suc's child
            suc.left = parent.left
            suc.right = parent.right
            parent.left = suc

        elif (parent.data < node.data): # right
            # replace parent's right to be successor
            if node.data != suc_parent.data:
                suc_parent.left = temp # restore its suc's parent to have suc's child
            suc.left = parent.left
            suc.right = parent.right
            parent.right = suc


    def _delete_with_predecessor(self, parent, node, pre):
        # pre could have a left child
        pre_parent = self._find_parent_node_recursive(pre.data, self.root)
        temp = pre.left # if predecessor has a left child
        pre_parent.right = temp # restore its pre's parent to have pre's child

        if (parent is None and node.data == self.root.data): # root node
            
            # set suc's pointers to point to root's left and right
            pre.left = self.root.left
            pre.right = self.root.right
            # new root is the suc
            self.root = pre
            
        elif (parent.data > node.data): # left
            # replace parent's left to be successor
            pre.left = parent.left
            pre.right = parent.right
            parent.left = pre

        elif (parent.data < node.data): # right
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
            print(self.root.data, item)
            # root node
            if (self.root.data == item):
                self.root = None
            # not root
            else:
                if (parent.data > item): # left
                    parent.left = None
                elif (parent.data < item): # right
                    parent.right = None
        # node has one child, left
        elif (node.right is None and node.left is not None):
            # root node
            if (self.root.data == item):
                self.root = node.left
            # not root: set parent's pointer to node's child
            else:
                if (parent.data > item): # left
                    parent.left = node.left
                elif (parent.data < item): # right
                    parent.right = node.left

        # node has one child, right
        elif (node.left is None and node.right is not None):
            # root node
            if (self.root.data == item):
                self.root = node.right
            # not root: set parent's pointer to node's child
            else:
                if (parent.data > item): # left
                    parent.left = node.right
                elif (parent.data < item): # right
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

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
            # self._traverse_in_order_iterative(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best case running time: O(logN) if balanced tree
        Worst case running time: O(N) if unbalanced tree"""
        if (node is None):
            return
        # Traverse left subtree, if it exists
        self._traverse_in_order_recursive(node.left, visit)
        # Visit this node's data with given function
        visit(node.data)
        # Traverse right subtree, if it exists
        self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best case running time: O(logN) if balanced tree
        Worst case running time: O(N) if unbalanced tree"""
        # Traverse in-order without using recursion (stretch challenge)
        # lets use a stack
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
                visit(node.data)
                # if it has any right nodes, add them to the stack
                if (node.right is not None):
                    temp = node.right
                    nodes.push(temp)
                    # add all of its left nodes
                    while (temp.left is not None):
                        nodes.push(temp.left)
                        temp = temp.left


    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
            # self._traverse_pre_order_iterative(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best case running time: O(logN) if balanced tree
        Worst case running time: O(N) if unbalanced tree"""
        if (node is None): return
        # Visit this node's data with given function
        visit(node.data)
        # Traverse left subtree, if it exists
        # self._traverse_pre_order_recursive(node.left, visit)
        self._traverse_pre_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
        self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best case running time: O(logN) if balanced tree
        Worst case running time: O(N) if unbalanced tree"""
        # Traverse pre-order without using recursion (stretch challenge)
        s = Stack()
        s.push(node)

        while (not s.is_empty()):
            node = s.pop()
            if node is not None:
                visit(node.data)
                if (node is not None):
                    s.push(node.right)
                if (node is not None):
                    s.push(node.left)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
            # self._traverse_post_order_iterative(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best case running time: O(logN) if balanced tree
        Worst case running time: O(N) if unbalanced tree"""
        if (node is None): return
        # Traverse left subtree, if it exists
        self._traverse_post_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
        self._traverse_post_order_recursive(node.right, visit)
        # Visit this node's data with given function
        visit(node.data)


    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Best case running time: O(logN) if balanced tree
        Worst case running time: O(N) if unbalanced tree"""
        # TODO: Traverse post-order without using recursion (stretch challenge)
        if (node is None):
            return
        s = Stack()
        s.push(node)
        
        seenlr = set() # already added node's left and right
        # visit left, then visit right, then visit node
        while (not s.is_empty()):
            node = s.pop()
            if (node not in seenlr):
                if (node.right is not None and node.left is not None):
                    s.push(node)
                    seenlr.add(node)
                    if (node.right is not None):
                        s.push(node.right)
                    if (node.left is not None):
                        s.push(node.left)
                else:
                    visit(node.data)
            else:
                visit(node.data)
                
            
        

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Best case running time: O(logN) if balanced tree
        Worst case running time: O(N) if unbalanced tree
        Space: 2**height"""
        # TODO: Create queue to store nodes not yet traversed in level-order
        queue = Queue()
        # TODO: Enqueue given starting node
        queue.enqueue(start_node)
        # TODO: Loop until queue is empty
        while (not queue.is_empty()):
            # TODO: Dequeue node at front of queue
            node = queue.dequeue()
            # TODO: Visit this node's data with given function
            visit(node.data)
            # TODO: Enqueue this node's left child, if it exists
            if (node.left is not None):
                queue.enqueue(node.left)
            # TODO: Enqueue this node's right child, if it exists
            if (node.right is not None):
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))
    print('height: {}'.format(tree.height()))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))
    print('height: {}'.format(tree.height()))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
