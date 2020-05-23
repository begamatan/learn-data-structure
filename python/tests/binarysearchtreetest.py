import sys
sys.path.append('..')

import unittest
from binarytree import Node
from binarysearchtree import BinarySearchTree

class BinarySearchTreeTest(unittest.TestCase):

    def test_binary_search_tree_is_created(self):
        new_node = Node(2)
        bst = BinarySearchTree(new_node)
        self.assertEqual(bst.val, new_node.val)
        self.assertEqual(bst.left, new_node.left)
        self.assertEqual(bst.right, new_node.right)

    def test_insert_node_to_left(self):
        new_node = Node(3)
        bst = BinarySearchTree(new_node)
        left_node = Node(2)
        bst.insert(bst, left_node)
        self.assertEqual(bst.left.val, 2)
        bst.insert(bst, Node(1))
        self.assertEqual(bst.left.left.val, 1)

    def test_insert_node_to_right(self):
        new_node = Node(3)
        bst = BinarySearchTree(new_node)
        right_node = Node(4)
        bst.insert(bst, right_node)
        self.assertEqual(bst.right.val, 4)
        bst.insert(bst, Node(5))
        self.assertEqual(bst.right.right.val, 5)

    def test_search_method(self):
        new_node = Node(3)
        bst = BinarySearchTree(new_node)
        right_node = Node(4)
        bst.insert(bst, right_node)
        left_node = Node(2)
        bst.insert(bst, left_node)
        res = bst.search(bst, 2)
        self.assertEqual(res.val, 2)
        res = bst.search(bst, 4)
        self.assertEqual(res.val, 4)
        res = bst.search(bst, 5)
        self.assertIsNone(res)

    def test_delete_method(self):
        bst = BinarySearchTree(Node(50))
        bst.insert(bst, Node(40))
        bst.insert(bst, Node(70))
        bst.insert(bst, Node(60))
        bst.insert(bst, Node(80))
        bst.delete(bst, 50)
        self.assertEqual(bst.val, 60)
        bst.delete(bst, 40)
        self.assertIsNone(bst.left)
        bst.delete(bst, 80)
        self.assertIsNone(bst.right.right)

if __name__ == "__main__":
    unittest.main()
