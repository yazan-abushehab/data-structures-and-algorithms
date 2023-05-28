from collections import deque

def breadth_first(tree):
  
    values = []

    queue = deque()

    if tree:
        queue.append(tree)

    while queue:
 
        node = queue.popleft()
        values.append(node.value)
       
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

   
    return values


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

result = breadth_first(root)
print(result)

