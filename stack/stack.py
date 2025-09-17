seedling_stack = []

# Add Items to Stack
seedling_stack.append("Seedling 1")
seedling_stack.append("Seedling 2")
seedling_stack.append("Seedling 3")

# Show stack contents
print("Seedling stack before planting:\n", seedling_stack)

# Stack pop()
planted = seedling_stack.pop()

# Show current contents
print("Planted:", planted)
print("Remaining stack:", seedling_stack)