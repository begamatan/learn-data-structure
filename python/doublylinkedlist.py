class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        #push node to head, reference https://www.geeksforgeeks.org/doubly-linked-list/
        new_node = Node(new_data)
        # set current head as new node next
        new_node.next = self.head
        if (self.head is not None):
            # if current head is not empty, set prev
            self.head.prev = new_node
        # finally set head to new node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        # prevent prev node to be null
        if prev_node is None:
            print("prev none cant be null")
            return
        # create new node on new data
        new_node = Node(new_data)
        # set new node next to prev node next
        new_node.next = prev_node.next
        # set new node prev to prev node
        new_node.prev = prev_node
        # set prev node next to new node
        prev_node.next = new_node
        if (new_node.next is not None):
            # update new node next prev to link with new node
            new_node.next.prev = new_node

    def insertBefore(self, next_node, new_data):
        if next_node is None:
            print("next none cant be null")
            return

        new_node = Node(new_data)
        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node
        if (new_node.prev is not None):
            # if not null, set new node prev next to new node
            new_node.prev.next = new_node
        else:
            # set new node to head
            self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            last = self.head
            while last.next is not None:
                last = last.next

            last.next = new_node
            new_node.prev = last

    def printList(self, node):
        while (node is not None):
            print(node.data)
            node = node.next

    def printReverse(self, node):
        while node is not None:
            last = node
            node = node.next

        while last is not None:
            print(last.data)
            last = last.prev

if __name__ == "__main__":
    llist = DoublyLinkedList()
    # 6->None
    llist.append(6)
    # 7->6->None
    llist.push(7)
    # 1->7->6->None
    llist.push(1)
    # 1->7->6->4
    llist.append(4)
    # 1->7->8->6->4
    llist.insertAfter(llist.head.next, 8)
    # 1->5->7->8->6->4
    llist.insertBefore(llist.head.next, 5)
    # print to proof
    llist.printList(llist.head)
    #print reverse
    llist.printReverse(llist.head)
