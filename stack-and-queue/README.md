# stack-and-queue
Stack : Create a Stack class that has a top property. It creates an empty Stack when instantiated.
Queue : Create a Queue class that has a front property. It creates an empty Queue when instantiated.

## Whiteboard Process
not required

## Approach & Efficiency
The time complexity of the code above is O(n^2), where "n" is the length of the input list. This is because the code contains two nested loops, and each loop iterates over the input list. Therefore, the total number of iterations is proportional to n * n, or n^2. Asymptotically, this is equivalent to O(n^2).

## Solution
    class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
    class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value
        
    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.top.value
        
    def is_empty(self):
        return self.top is None
        
    class Queue:
    def __init__(self):
        self.front = None
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
        else:
            current_node = self.front
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        popped_value = self.front.value
        self.front = self.front.next
        return popped_value
        
    def peek(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.front.value
        
    def is_empty(self):
        return self.front is None
