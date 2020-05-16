class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        print(True if len(self.data) is 0 else False)

    def push(self, new_data):
        self.data.append(new_data)

    def pop(self):
        if (self.isEmpty()):
            print('Stack is empty')
            return
        self.data.pop()

    def peek(self):
        print(self.data[len(self.data) - 1])

    def printStack(self):
        for stack in self.data:
            print(stack)

if __name__ == "__main__":
    stack = Stack()
    # print(stack.isEmpty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())
    stack.pop()
    stack.printStack()
