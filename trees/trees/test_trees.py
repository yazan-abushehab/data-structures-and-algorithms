import unittest
from trees.trees import BinarySearchTree,BinaryTree

class BinarySearchTreeTests(unittest.TestCase):
    def test_instantiate_empty_tree(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst.root)

    def test_instantiate_tree_with_single_node(self):
        bst = BinarySearchTree()
        bst.add(5)
        self.assertEqual(bst.root.value, 5)

    def test_add_left_and_right_child_to_node(self):
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        self.assertEqual(bst.root.left.value, 3)
        self.assertEqual(bst.root.right.value, 7)

    def test_preorder(self):
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(1)
        bst.add(4)
        bst.add(6)
        bst.add(8)
        expected = [5, 3, 1, 4, 7, 6, 8]
        self.assertEqual(bst.preorder(bst.root), expected)

    def test_inorder(self):
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(1)
        bst.add(4)
        bst.add(6)
        bst.add(8)
        expected = [1, 3, 4, 5, 6, 7, 8]
        self.assertEqual(bst.inorder(bst.root), expected)

    def test_postorder(self):
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(1)
        bst.add(4)
        bst.add(6)
        bst.add(8)
        expected = [1, 4, 3, 6, 8, 7, 5]
        self.assertEqual(bst.postorder(bst.root), expected)

    def test_contains_existing_value(self):
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        self.assertTrue(bst.contains(3))

    def test_contains_non_existing_value(self):
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        self.assertFalse(bst.contains(10))


if __name__ == '__main__':
    unittest.main()
