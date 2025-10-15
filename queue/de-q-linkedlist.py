class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleEndedQueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue_front(self, item):
        """Insert at the front."""
        new_node = DNode(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        print(f"Enqueued (front): {item}")

    def enqueue_rear(self, item):
        """Insert at the rear."""
        new_node = DNode(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued (rear): {item}")

    def dequeue_front(self):
        """Remove from the front."""
        if self.is_empty():
            print("Queue is empty! Nothing to remove from front.")
            return None
        removed_item = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        print(f"Dequeued (front): {removed_item}")
        return removed_item

    def dequeue_rear(self):
        """Remove from the rear."""
        if self.is_empty():
            print("Queue is empty! Nothing to remove from rear.")
            return None
        removed_item = self.rear.data
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None
        print(f"Dequeued (rear): {removed_item}")
        return removed_item

    def is_empty(self):
        return self.front is None

    def display(self):
        if self.is_empty():
            print("Deque is empty.")
            return
        current = self.front
        items = []
        while current:
            items.append(current.data)
            current = current.next
        print("Deque (front → rear):", items)


if __name__ == "__main__":
    print("\n--- Double-Ended Queue (Linked List) ---")
    q = DoubleEndedQueueLinkedList()
    q.enqueue_rear("Last")
    q.enqueue_front("First")
    q.display()
    q.dequeue_front()
    q.display()