class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self, root):
        if self.root is None:
            return []
        list=[]
        def recursive (root):
            list.append(root.value)
            if root.left : recursive(root.left)
            if root.right : recursive(root.right)
        recursive(root)    
        return list

    def inorder(self, root):
        if self.root is None:
            return []
        list=[]
        def recursive (root):
            if root.left : recursive(root.left)
            list.append(root.value)
            if root.right : recursive(root.right)
        recursive(root)    
        return list

    def postorder(self, root):
        if self.root is None:
            return []
        list=[]
        def recursive (root):
            if root.left : recursive(root.left)
            if root.right : recursive(root.right)
            list.append(root.value)
        recursive(root)    
        return list


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def contains(self, value):
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._contains_recursive(node.left, value)
        else:
            return self._contains_recursive(node.right, value)

# Creating a binary search tree
bst = BinarySearchTree()

# Adding nodes to the binary search tree
bst.add(5)
bst.add(3)
bst.add(7)
bst.add(1)
bst.add(4)
bst.add(6)
bst.add(8)

# Checking if a value is in the tree
print(bst.contains(4))  # True
print(bst.contains(9))  # False

# Performing depth first traversals
print(bst.preorder(bst.root))    # [5, 3, 1, 4, 7, 6, 8]
print(bst.inorder(bst.root))     # [1, 3, 4, 5, 6, 7, 8]
print(bst.postorder(bst.root))   # [1, 4, 3, 6, 8, 7, 5]
