import sys
sys.path.append('..')

import unittest
from binarytree import Node

class BinaryTreeTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_root_is_created(self):
        root = Node(1)
        self.assertEqual(root.val, 1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_can_insert_left_child_to_root(self):
        root = Node(1)
        left_child = Node(2)
        root.left = left_child
        self.assertEqual(root.left.val, 2)

    def test_can_insert_right_child_to_root(self):
        root = Node(1)
        right_child = Node(3)
        root.right = right_child
        self.assertEqual(root.right.val, 3)

if __name__ == '__main__':
    unittest.main()
