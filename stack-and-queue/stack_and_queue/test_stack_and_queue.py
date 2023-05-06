import pytest

from stack_and_queue.stack_and_queue import Stack, Queue


def test_push_one_item_to_stack():
    s = Stack()
    s.push(1)
    assert s.top.value == 1

def test_push_multiple_items_to_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.top.value == 3
    assert s.top.next.value == 2
    assert s.top.next.next.value == 1

def test_pop_from_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.top.value == 2
    assert s.pop() == 2
    assert s.top.value == 1

def test_empty_stack_after_multiple_pops():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.pop()
    s.pop()
    assert s.is_empty()

def test_peek_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.peek() == 3
    assert s.top.value == 3

def test_instantiate_empty_stack():
    s = Stack()
    assert s.is_empty()

def test_pop_from_empty_stack_raises_exception():
    s = Stack()
    with pytest.raises(Exception):
        s.pop()

def test_peek_empty_stack_raises_exception():
    s = Stack()
    with pytest.raises(Exception):
        s.peek()

def test_enqueue_one_item_to_queue():
    q = Queue()
    q.enqueue(1)
    assert q.front.value == 1

def test_enqueue_multiple_items_to_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.front.value == 1
    assert q.front.next.value == 2
    assert q.front.next.next.value == 3

def test_dequeue_from_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.front.value == 2
    assert q.dequeue() == 2
    assert q.front.value == 3

def test_peek_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.peek() == 1
    assert q.front.value == 1

def test_empty_queue_after_multiple_dequeues():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    assert q.is_empty()

def test_instantiate_empty_queue():
    q = Queue()
    assert q.is_empty()

def test_dequeue_from_empty_queue_raises_exception():
    q = Queue()
    with pytest.raises(Exception):
        q.dequeue()

def test_peek_empty_queue_raises_exception():
    q = Queue()
    with pytest.raises(Exception):
        q.peek()
