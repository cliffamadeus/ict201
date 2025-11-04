class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, target, element):
        current = self.head
        while current:
            if current.data == target:
                new_node = Node(element)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with value {target} not found.")

    def delete(self, element):
        current = self.head
        previous = None

        while current:
            if current.data == element:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                print(f"Deleted node with value {element}.")
                return
            previous = current
            current = current.next

        print(f"Node with value {element} not found.")

    def search(self, element):
        current = self.head
        index = 0
        while current:
            if current.data == element:
                print(f"Element {element} found at node {index}.")
                return current
            current = current.next
            index += 1
        print(f"Element {element} not found.")
        return None

    def traverse(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        current = self.head
        print("Linked list elements:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
ll = LinkedList()

# Insert elements
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_end(40)
ll.insert_at_end(50)
ll.traverse()

# Insert after a given node
ll.insert_after(40, 45)
ll.traverse()

# Search for an element
ll.search(20)
ll.search(100)

# Delete an element
ll.delete(30)
ll.traverse()
