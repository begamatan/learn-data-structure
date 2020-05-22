from binarytree import Node

class BinarySearchTree:
    def __init__(self, node):
        self.val = node.val
        self.left = node.left
        self.right = node.right

    def insert(self, root, node):
        if node.val < root.val:
            if root.left is None:
                root.left = node
            else:
                self.insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right, node)

    def search(self, root, key):
        if root is None or root.val is key:
            return root

        if key < root.val:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

if __name__ == "__main__":
    bst = BinarySearchTree(Node(3))
    bst.insert(bst, Node(2))
    bst.insert(bst, Node(4))
    bst.inorder(bst)
