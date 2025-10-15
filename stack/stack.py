class Stack:
    def __init__(self):
        self.stack = []  # initialize an empty stack

    def push(self, item):
        """Add a to the stack."""
        self.stack.append(item)
        print(f"Added: {item}")

    def pop(self):
        """Remove the top from the stack."""
        if not self.is_empty():
            planted = self.stack.pop()
            print(f"Planted: {planted}")
            return planted
        else:
            print("No seedlings left to plant!")
            return None

    def peek(self):
        """View the top  without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Display the current stack."""
        print("Current  stack:", self.stack)


# Example usage
if __name__ == "__main__":
    seed_stack = Stack()

    # Add seedlings
    seed_stack.push(" 1")
    seed_stack.push(" 2")
    seed_stack.push(" 3")

    # Display before planting
    seed_stack.display()

    # Plant one seedling
    seed_stack.pop()

    # Display after planting
    seed_stack.display()
