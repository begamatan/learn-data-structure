# reference https://www.geeksforgeeks.org/circular-singly-linked-list-insertion/

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self, new_data):
        new_node = Node(new_data)
        # set last pointer to new node
        self.last = new_node
        # because it's empty, last next will be itself
        self.last.next = self.last

    def addBegin(self, new_data):
        new_node = Node(new_data)
        # set new node next to last next
        new_node.next = self.last.next
        # set self last next to new node
        self.last.next = new_node

    def addEnd(self, new_data):
        new_node = Node(new_data)
        # set new node next to last pointer next
        new_node.next = self.last.next
        # set last next to new node
        self.last.next = new_node
        # set last pointer to new node
        self.last = new_node

    def addAfter(self, prev_data, new_data):
        if (self.last == None):
            return
        # if prev_data is last, use add end instead
        if prev_data is self.last.data:
            self.addEnd(new_data)
            return
        new_node = Node(new_data)
        temp = self.last
        while temp:
            temp = temp.next
            if temp.data is prev_data:
                break
        # set new node next to prev node next
        new_node.next = temp.next
        # set prev node next to new node
        temp.next = new_node

    def printList(self):
        if self.last is None:
            print("empty list")
            return
        temp = self.last.next
        while temp:
            print(temp.data)
            temp = temp.next
            if temp == self.last.next:
                return

llist = CircularLinkedList()
llist.addToEmpty(6)
llist.addBegin(4)
llist.addBegin(2)
llist.addEnd(8)
llist.addEnd(12)
llist.addAfter(8, 10)
# 2 4 6 8 10 12
llist.printList()
