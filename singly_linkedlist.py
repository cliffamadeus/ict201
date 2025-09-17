class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new = Node(value)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def display(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.value))
            temp = temp.next
        print("Linked List:", " -> ".join(nodes))

# Example usage
ll = LinkedList()
ll.add_node("Node 1")
ll.display()
ll.add_node("Node 2")
ll.display()
ll.add_node("Node 3")
ll.display()
