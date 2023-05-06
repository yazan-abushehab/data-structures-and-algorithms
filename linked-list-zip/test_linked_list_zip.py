import unittest

from linked_list_zip.linked_list_zip import ListNode, linked_list_zip

class TestLinkedListZip(unittest.TestCase):
    def test_linked_list_zip(self):
        # Test case 1
        l1 = ListNode(1, ListNode(3, ListNode(5)))
        l2 = ListNode(2, ListNode(4, ListNode(6)))
        result = linked_list_zip(l1, l2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)
        self.assertEqual(result.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.val, 5)
        self.assertEqual(result.next.next.next.next.next.val, 6)
        self.assertIsNone(result.next.next.next.next.next.next)

        # Test case 2
        l1 = ListNode(1, ListNode(3, ListNode(5)))
        l2 = ListNode(2, ListNode(4))
        result = linked_list_zip(l1, l2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)
        self.assertEqual(result.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.val, 5)
        self.assertIsNone(result.next.next.next.next.next)

        # Test case 3
        l1 = None
        l2 = ListNode(2, ListNode(4))
        result = linked_list_zip(l1, l2)
        self.assertEqual(result.val, 2)
        self.assertEqual(result.next.val, 4)
        self.assertIsNone(result.next.next)

        # Test case 4
        l1 = ListNode(1)
        l2 = ListNode(2)
        result = linked_list_zip(l1, l2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertIsNone(result.next.next)

if __name__ == '__main__':
    unittest.main()
