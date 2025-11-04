class Array:
    def __init__(self, capacity=10):
        self.data = [None] * capacity  # fixed size array
        self.size = 0

    def insert(self, index, element):
        if index < 0 or index > self.size:
            print("Invalid index!")
            return
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = element
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index!")
            return
        deleted = self.data[index]
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1
        print(f"Deleted element {deleted}")

    def update(self, index, element):
        if index < 0 or index >= self.size:
            print("Invalid index!")
            return
        self.data[index] = element

    def search(self, element):
        for i in range(self.size):
            if self.data[i] == element:
                print(f"Element {element} found at index {i}")
                return i
        print(f"Element {element} not found")
        return -1

    def traverse(self):
        if self.size == 0:
            print("Array is empty")
        else:
            print("Array elements:", end=" ")
            for i in range(self.size):
                print(self.data[i], end=" ")
            print()


# Example usage
arr = Array()

# Insert elements
arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
arr.traverse()

# Update element
arr.update(1, 25)
arr.traverse()

# Search element
arr.search(30)
arr.search(50)

# Delete element
arr.delete(0)
arr.traverse()
