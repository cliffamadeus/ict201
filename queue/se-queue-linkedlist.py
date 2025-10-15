class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleEndedQueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        """Insert at the rear."""
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued (rear): {item}")

    def dequeue(self):
        """Remove from the front."""
        if self.is_empty():
            print("Queue is empty! Nothing to dequeue.")
            return None
        removed_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued (front): {removed_item}")
        return removed_item

    def is_empty(self):
        return self.front is None

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        items = []
        while current:
            items.append(current.data)
            current = current.next
        print("Queue (front → rear):", items)

if __name__ == "__main__":

    print("\n--- Single-Ended Queue (Linked List) ---")
    q = SingleEndedQueueLinkedList()
    q.enqueue("X")
    q.enqueue("Y")
    q.display()
    q.dequeue()
    q.display()