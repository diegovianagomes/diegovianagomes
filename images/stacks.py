class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def empty(self):
        return self.top == -1

    def full(self):
        return self.top == self.capacity - 1

    def push(self, element):
        if self.full():
            print("Error: The stack is full")
        else:
            self.top += 1
            self.stack[self.top] = element
            print(f"Element {element} added to the top {self.top}")

    def pop(self):
        if self.empty():
            print("Error: The stack is empty")
        else:
            element = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(f"Element {element} removed from top {self.top + 1}")
            return element

    def show(self):
        if self.empty():
            print("Empty stack")
        else:
            print("Current stack state:")
            for i in range(self.top + 1):
                print(f"Position {i + 1}: {self.stack[i]}")

capacity = 7
stack = Stack(capacity)

stack.push(15)
stack.push(6)
stack.push(2)
stack.push(9)
stack.show()


stack.pop()
stack.show()