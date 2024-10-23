class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.capacity

    def enqueue(self, element):
        if self.full():
            print("Error: The queue is full")
        else:
            self.queue[self.tail] = element
            self.tail = (self.tail + 1) % self.capacity
            self.size += 1

            print(f"Element {element} added to queue.")

    def dequeue(self):
        if self.empty():
            print("Error: Queue is empty")
        else:
            element = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.capacity
            self.size -= 1
            print(f"Element {element} removed from queue.")

            return element

    def show(self):
        if self.empty():
            print("Empty queue")
        else:
            print("Current queue:")
            i = self.head
            for _ in range(self.size):
                print(self.queue[i], end=" ")
                i = (i + 1) % self.capacity
            print()


queue = Queue(5)

queue.enqueue(15)
queue.enqueue(6)
queue.enqueue(2)
queue.enqueue(9)
queue.enqueue(4)

"""
Element 15 added to queue.
Element 6 added to queue.
Element 2 added to queue.
Element 9 added to queue.
Element 4 added to queue.
Current queue:
15 6 2 9 4"""
queue.show() 

queue.dequeue()
queue.show()

"""
Element 15 removed from queue.
Current queue:
6 2 9 4
"""
