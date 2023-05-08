import pytest
from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue

def test_pseudo_queue():
    # Test enqueue method
    q = PseudoQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.stack1.items == [1, 2, 3]
    
    # Test dequeue method
    assert q.dequeue() == 1
    assert q.stack1.items == []
    assert q.stack2.items == [3, 2]
    
    # Test alternating enqueue and dequeue operations
    q.enqueue(4)
    q.enqueue(5)
    assert q.dequeue() == 2
    q.enqueue(6)
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.stack1.items == []
    assert q.stack2.items == [6, 5]
    
    # Test dequeue on an empty PseudoQueue
    q = PseudoQueue()
    assert q.dequeue() == None
