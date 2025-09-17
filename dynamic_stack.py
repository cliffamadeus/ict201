# Dynamic stack implementation for seedlings
seedling_stack = []

while True:
    print("\n--- Seedling Stack Menu ---")
    print("1. Add a seedling")
    print("2. Plant a seedling (pop)")
    print("3. View seedling stack")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        seedling = input("Enter seedling name: ")
        seedling_stack.append(seedling)
        print(f"Added: {seedling}")

    elif choice == "2":
        if seedling_stack:
            planted = seedling_stack.pop()
            print(f"Planted: {planted}")
        else:
            print("No seedlings left to plant!")

    elif choice == "3":
        if seedling_stack:
            print("Current Seedling Stack:", seedling_stack)
        else:
            print("Stack is empty.")

    elif choice == "4":
        print("Exiting... 🌱")
        break

    else:
        print("Invalid choice. Please try again.")
