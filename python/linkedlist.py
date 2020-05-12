# reference https://www.geeksforgeeks.org/linked-list-set-1-introduction/ and https://www.tutorialspoint.com/python/python_nodes.htm
class Node:
    # __init__ is like __construct in php
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


# https: // www.freecodecamp.org/news/whats-in-a-python-s-name-506262fe61e8/
# When you run this file, __name__ is equal to __main__.
# When you import it in other script, __name__ is equal to this script filename (e.g. linkedlist)
if __name__ == "__main__":
    # empty list
    llist = LinkedList()
    # set list head to Node with data = 1
    # Node next is null/none
    llist.head = Node(1)

    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    # third.next is null/none

    # print list
    llist.printList()

    # so list is started with head and linked to next node until it's end
