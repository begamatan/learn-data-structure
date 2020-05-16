class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return True if self.head is None else False

    def push(self, new_data):
        new_node = StackNode(new_data)
        # set next to current head
        new_node.next = self.head
        # set current head to new node
        self.head = new_node

    def pop(self):
        # if stack is empty print and return
        if self.isEmpty():
            print('Stack is empty')
            return
        # set head to current head next
        self.head = self.head.next

    def peek(self):
        # if stack is empty print and return
        if self.isEmpty():
            print('Stack is empty')
            return
        # print latest inserted data
        print(self.head.data)

    def printStack(self, head):
        # print from oldest item / first in using recursive
        if head.next is None:
            print(head.data)
            return

        self.printStack(head.next)
        print(head.data)

if __name__ == "__main__":
    stack = Stack()
    stack.pop()
    stack.peek()
    stack.push(1)
    stack.push(2)
    stack.peek()
    stack.push(3)
    stack.pop()
    stack.peek()
    stack.printStack(stack.head)
