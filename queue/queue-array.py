class ArrayQueue:
    def __init__(self):
        self.queue = []

    def peek(self):
        """View the front item without removing it."""
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def display(self):
        """Display current queue."""
        print("Current queue (front → rear):", self.queue)

if __name__ == "__main__":
    print("\n--- Array Queue ---")
    aq = ArrayQueue()
    aq.enqueue("A")
    aq.enqueue("B")
    aq.display()
    aq.dequeue()
    aq.display()