class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_zip(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy
    current1, current2 = l1, l2
    
    while current1 and current2:
        current.next = current1
        current1 = current1.next
        current = current.next
        current.next = current2
        current2 = current2.next
        current = current.next
        
    if current1:
        current.next = current1
        
    if current2:
        current.next = current2
        
    return dummy.next
