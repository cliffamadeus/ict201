class DoubleEndedQueueArray:
    def __init__(self):
        self.queue = []

    def enqueue_front(self, item):
        """Insert item at the front."""
        new_queue = [item] + self.queue
        self.queue = new_queue
        print(f"Enqueued (front): {item}")

    def enqueue_rear(self, item):
        """Insert item at the rear."""
        new_queue = self.queue + [item]
        self.queue = new_queue
        print(f"Enqueued (rear): {item}")

    def dequeue_front(self):
        """Remove item from the front."""
        if self.is_empty():
            print("Queue is empty! Nothing to remove from front.")
            return None
        removed_item = self.queue[0]
        self.queue = [self.queue[i] for i in range(1, len(self.queue))]
        print(f"Dequeued (front): {removed_item}")
        return removed_item

    def dequeue_rear(self):
        """Remove item from the rear."""
        if self.is_empty():
            print("Queue is empty! Nothing to remove from rear.")
            return None
        removed_item = self.queue[-1]
        self.queue = [self.queue[i] for i in range(len(self.queue) - 1)]
        print(f"Dequeued (rear): {removed_item}")
        return removed_item

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Deque (front → rear):", self.queue)


if __name__ == "__main__":
    print("\n--- Double-Ended Queue (Array) ---")
    q = DoubleEndedQueueArray()
    q.enqueue_rear("1")
    q.enqueue_front("0")
    q.display()
    q.dequeue_rear()
    q.display()