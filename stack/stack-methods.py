class Stack:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.top_index = -1
        self.capacity = capacity

    def push(self, element):
        if self.top_index >= self.capacity - 1:
            print("Stack overflow!")
            return
        self.top_index += 1
        self.data[self.top_index] = element

    def pop(self):
        if self.is_empty():
            print("Stack underflow!")
            return None
        element = self.data[self.top_index]
        self.data[self.top_index] = None
        self.top_index -= 1
        return element

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.data[self.top_index]

    def is_empty(self):
        return self.top_index == -1

    def size(self):
        return self.top_index + 1

    def traverse(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):", end=" ")
            for i in range(self.top_index, -1, -1):
                print(self.data[i], end=" ")
            print()


# Example usage
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.traverse()

print("Top element:", stack.peek())
print("Popped element:", stack.pop())
stack.traverse()
print("Stack size:", stack.size())
