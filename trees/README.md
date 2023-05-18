# trees 
Node
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
Binary Tree
Create a Binary Tree class
Define a method for each of the depth first traversals:
pre order
in order
post order
Each depth first traversal method should return an array of values, ordered appropriately.
Binary Search Tree
Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
Add
Arguments: value
Return: nothing
Adds a new node with that value in the correct location in the binary search tree.
Contains
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.

<br>

## Whiteboard Process
not require

<br>

## Approach & Efficiency

>- BinaryTree
Time -> O(1)  It has a constant time complexity.
Space -> O(1) It does not depend on the size of the tree or the number of nodes, so the space complexity is constant.

>- BinarySearchTree
Time -> O(n)  The method visits each node in the tree exactly once, resulting in a linear time complexity since it needs to process all the nodes.
Space -> O(n) The space complexity for the traversal methods depends on the number of nodes in the tree.

<br>

## Solution
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self, node):
        if node is None:
            return []
        result = [node.value]
        result += self.preorder_traversal(node.left)
        result += self.preorder_traversal(node.right)
        return result

    def inorder_traversal(self, node):
        if node is None:
            return []
        result = self.inorder_traversal(node.left)
        result.append(node.value)
        result += self.inorder_traversal(node.right)
        return result

    def postorder_traversal(self, node):
        if node is None:
            return []
        result = self.postorder_traversal(node.left)
        result += self.postorder_traversal(node.right)
        result.append(node.value)
        return result


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
