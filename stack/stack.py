class Stack:
    def __init__(self):
        self.stack = []  # initialize an empty stack

    def push(self, item):
        """Add an item to the top of the stack (without append)."""
        # create a new list one element longer
        new_stack = [None] * (len(self.stack) + 1)
        for i in range(len(self.stack)):
            new_stack[i] = self.stack[i]
        new_stack[len(self.stack)] = item
        self.stack = new_stack
        print(f"Added: {item}")

    def pop(self):
        """Remove the top item from the stack (without pop)."""
        if not self.is_empty():
            planted = self.stack[-1]  # get the last element
            # create a new list without the last element
            new_stack = [self.stack[i] for i in range(len(self.stack) - 1)]
            self.stack = new_stack
            print(f"Planted: {planted}")
            return planted
        else:
            print("No seedlings left to plant!")
            return None

    def peek(self):
        """View the top item without removing it."""
        if not self.is_empty():
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Display the current stack."""
        print("Current stack:", self.stack)


# Example usage
if __name__ == "__main__":
    seed_stack = Stack()

    # Add seedlings
    seed_stack.push("Seedling 1")
    seed_stack.push("Seedling 2")
    seed_stack.push("Seedling 3")

    # Display before planting
    seed_stack.display()

    # Plant one seedling
    seed_stack.pop()

    # Display after planting
    seed_stack.display()
