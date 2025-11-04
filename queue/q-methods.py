class Queue:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.front_index = 0
        self.rear_index = -1
        self.size_count = 0
        self.capacity = capacity

    def enqueue(self, element):
        if self.size_count == self.capacity:
            print("Queue overflow!")
            return
        self.rear_index = (self.rear_index + 1) % self.capacity
        self.data[self.rear_index] = element
        self.size_count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow!")
            return None
        element = self.data[self.front_index]
        self.data[self.front_index] = None
        self.front_index = (self.front_index + 1) % self.capacity
        self.size_count -= 1
        return element

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.data[self.front_index]

    def is_empty(self):
        return self.size_count == 0

    def size(self):
        return self.size_count

    def traverse(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements (front to rear):", end=" ")
            i = self.front_index
            count = 0
            while count < self.size_count:
                print(self.data[i], end=" ")
                i = (i + 1) % self.capacity
                count += 1
            print()


# Example usage
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.traverse()

print("Front element:", queue.peek())
print("Dequeued element:", queue.dequeue())
queue.traverse()
print("Queue size:", queue.size())
