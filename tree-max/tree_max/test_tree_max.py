from tree_max.tree_max import BinaryTree



def test_find_maximum_value():
    # Create a binary tree
    tree = BinaryTree(10)
    tree.left = BinaryTree(5)
    tree.right = BinaryTree(15)
    tree.left.left = BinaryTree(3)
    tree.left.right = BinaryTree(8)
    tree.right.left = BinaryTree(12)
    tree.right.right = BinaryTree(20)

    # Test the find_maximum_value() method
    assert tree.find_maximum_value() == 20

    # Additional test cases
    assert BinaryTree(None).find_maximum_value() is None
    assert BinaryTree(7).find_maximum_value() == 7
    assert BinaryTree(0).find_maximum_value() == 0
