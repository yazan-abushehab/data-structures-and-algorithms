class Node:
    def __init__(self, value):
        """Initialize a new node with the given value and set the next node to None."""
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list with a head node set to None."""
        self.head = None

    def insert(self, value):
        """Insert a new node with the given value at the beginning of the linked list."""
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def includes(self, key):
        """
        Check if a node with the given key value exists in the linked list.
        Return True if the node is found, False otherwise.
        """
        temp = self.head
        if temp is None:
            return False
        while temp is not None:
            if temp.value == key:
                return True
            temp = temp.next
        if temp is None:
            return False

    def append(self, value):
        """Add a new node with the given value to the end of the linked list."""
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def insert_after(self, target, value):
        """
        Insert a new node with the given value immediately after the first node in the list with the target value.
        If the target value is not found, print an error message and do nothing.
        """
        if self.includes(target):
            node = Node(value)
            if self.head is None:
                self.insert(value)
            else:
                current = self.head
                while current.value != target:
                    current = current.next
                node.next = current.next
                current.next = node
        else:
            print("Error: the target value does not exist in the linked list.")

    def insert_before(self, target, value):
        """
        Insert a new node with the given value immediately before the first node in the list with the target value.
        If the target value is not found, print an error message and do nothing.
        """
        if self.includes(target):
            node = Node(value)
            if self.head is None or self.head.value == target:
                self.insert(value)
            else:
                current = self.head
                while current.next.value != target:
                    current = current.next
                node.next = current.next
                current.next = node
        else:
            print("Error: the target value does not exist in the linked list.")

    def __str__(self):
        """Return a string representation of the linked list, with each node separated by '->'."""
        output = ""
        if self.head is None:
            output = "Empty LinkedList"
        else:
            current = self.head
            while current:
                output += f'{current.value} -> '
                current = current.next
            output += "Null"
        return output
