def delete(self, item):
    node = self._find_node_recursive(item, self.root)
    # not found
    if (node is None):
        return
    # find parent of node
    parent = self._find_parent_node_recursive(item, self.root)

    # node has no child
    if (node.is_leaf()):
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
    elif (node.isbranch()):
       # predecessor and successor, use whichever is not None
        pre = self._get_predecessor(node) # has no right node
        suc = self._get_successor(node) # has no left node
        if (pre.height() > suc.height()):
            self._delete_with_predecessor(parent, node, pre)
        else:
            self._delete_with_successor(parent, node, suc)

def _delete_with_successor(self, parent, node, suc):
    # suc could have a right child
    suc_parent = self._find_parent_node_recursive(suc.data, self.root)
    temp = suc.right # if successor has a right child
    suc_parent.left = temp # restore its suc's parent to have suc's child

    if (parent is None and node.data == self.root.data): # root node
        
        # set suc's pointers to point to root's left and right
        suc.left = self.root.left
        suc.right = self.root.right
        # new root is the suc
        self.root = suc
        
    elif (parent.data > node.data): # left
        # replace parent's left to be successor
        suc.left = parent.left
        suc.right = parent.right
        parent.left = suc

    elif (parent.data < node.data): # right
        # replace parent's right to be successor
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
        self.root = suc
        
    elif (parent.data > node.data): # left
        # replace parent's left to be successor
        pre.left = parent.left
        pre.right = parent.right
        parent.left = suc

    elif (parent.data < node.data): # right
        # replace parent's right to be successor
        pre.left = parent.left
        pre.right = parent.right
        parent.right = suc