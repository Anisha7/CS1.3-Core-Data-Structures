#!python
from linkedlist import LinkedList

class BinaryNode(object):
    
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

# borrows functions that are implemented in the same way from linked list
# creates its own append, prepend, insert, and delete functions to factor in the prev
class DoublyLinkedList(LinkedList):
    
    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) if first or last index
        Worst case running time: O(N) if last-1 index or doesn't exist"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        
        # if inserting in beginning
        if index == 0:
            self.prepend(item)
            return
        # if inserting at end
        if index == self.size:
            self.append(item)
            return

        # Find the node at the given index and insert item before it
        curr = self.head
        curr_index = 0
        

        while (curr_index != index and curr != None):
            curr = curr.next
            curr_index += 1
        
        if curr == None:
            raise ValueError('Item does not exist!!!: {}'.format(index))
        assert curr_index == index
        # found node before curr index
        # insert before this node
        new_node = BinaryNode(item)
        new_node.next = curr # initialize next for new_node
        temp = curr.prev # hold list before node
        temp.next = new_node # add new node to its next
        new_node.prev = temp # initialize prev for new_node
        curr.prev = new_node # add new node behind our curr

        # update size after inserting
        self.size += 1

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1) always"""
        # Create a new node to hold the given item
        new_node = BinaryNode(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            new_node.prev = self.tail
            self.tail.next = new_node
        # Update tail to new node regardless
        self.tail = new_node

        # add to size
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: O(1) always"""
        # Create a new node to hold the given item
        new_node = BinaryNode(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            self.head.prev = new_node
            new_node.next = self.head
        # Update head to new node regardless
        self.head = new_node

        # add to size
        self.size += 1

    def findNode(self, item):
        """Return an node from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if node.data == item:  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if its the first or last value
        Worst case running time: O(N) if its the second to last value or doesn't exist"""
        node = self.findNode(item)
        # found item
        if (node != None):
            self.size -= 1
            # if head node
            if (node.data == self.head.data):
                self.head = self.head.next
                if (self.head != None):
                    self.head.prev = None
                if (self.head == None):
                    self.tail = None

            # if tail node
            elif (node.data == self.tail.data):
                self.tail = self.tail.prev
                self.tail.next = None
            
            # if middle node
            else:
                # alter pointers to remove curr node
                node.next.prev = node.prev # change next's prev
                node.prev.next = node.next # change prev's next

        # did not find item
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))