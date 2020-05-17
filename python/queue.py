# reference https://www.geeksforgeeks.org/queue-set-1introduction-and-array-implementation/
class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.q = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.size is self.capacity

    def isEmpty(self):
        return self.size is 0

    def enqueue(self, item):
        if self.isFull():
            print('Queue is full')
            return
        # it's equal to the first queue
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = item
        self.size = self.size + 1

    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty')
        # it's equal to next of current front
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1

    def que_front(self):
        if self.isEmpty():
            print('Queue is empty')
            return
        print(self.q[self.front])

    def que_rear(self):
        if self.isEmpty():
            print('Queue is empty')
            return
        print(self.q[self.rear])


if __name__ == "__main__":
    queue = Queue(4)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    # this should print queue full
    queue.enqueue(5)
    # 1
    queue.que_front()
    # 4
    queue.que_rear()

    queue.dequeue()
    # 2
    queue.que_front()

    queue.enqueue(5)
    # 2
    queue.que_front()
    # 5
    queue.que_rear()

    queue.dequeue()
    # 3
    queue.que_front()

    queue.dequeue()
    # 4
    queue.que_front()

    queue.dequeue()
    # 5
    queue.que_front()
    # 5 too
    queue.que_rear()

    queue.enqueue(6)
    # 5
    queue.que_front()
    # 6
    queue.que_rear()
