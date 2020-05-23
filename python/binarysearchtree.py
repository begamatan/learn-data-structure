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

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self.delete(root.left, key)

        elif key > root.val:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            else:
                temp = self.getMinVal(root.right)
                root.val = temp.val
                root.right = self.delete(root.right, temp.val)
                return root

        return root

    def getMinVal(self, root):
        minval = root
        while minval.left is not None:
            minval = minval.left
        return minval

if __name__ == "__main__":
    bst = BinarySearchTree(Node(50))
    bst.insert(bst, Node(40))
    bst.insert(bst, Node(60))
    bst.insert(bst, Node(70))
    bst.insert(bst, Node(80))
    bst.inorder(bst)
