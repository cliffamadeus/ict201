# Node class to represent each element in the stack
class Node:
    def __init__(self, data):
        self.data = data      # holds the item
        self.next = None      # pointer to the next node


# Stack class using linked list
class LinkedListStack:
    def __init__(self):
        self.top = None  # represents the top node of the stack

    def push(self, item):
        """Add a new item to the top of the stack."""
        new_node = Node(item)
        new_node.next = self.top  # link the old top to new node
        self.top = new_node       # update top pointer
        print(f"Added: {item}")

    def pop(self):
        """Remove the top item from the stack."""
        if self.is_empty():
            print("Stack is empty! Nothing to remove.")
            return None
        else:
            removed_item = self.top.data
            self.top = self.top.next  # move top pointer down
            print(f"Removed: {removed_item}")
            return removed_item

    def peek(self):
        """View the top item without removing it."""
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def display(self):
        """Display all items in the stack."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            current = self.top
            elements = []
            while current:
                elements.append(current.data)
                current = current.next
            print("Current stack (top → bottom):", elements)


# Example usage
if __name__ == "__main__":
    seedlings = LinkedListStack()

    # Add items
    seedlings.push("Seedling 1")
    seedlings.push("Seedling 2")
    seedlings.push("Seedling 3")

    # Display before removing
    seedlings.display()

    # Remove one item
    seedlings.pop()

    # Display after removing
    seedlings.display()
