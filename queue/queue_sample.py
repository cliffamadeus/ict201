from collections import deque

# Initialize patrol queue
patrol_queue = deque()

# Add boats to the queue (enqueue)
patrol_queue.append("Boat 1")
patrol_queue.append("Boat 2")
patrol_queue.append("Boat 3")

# Show patrol order
print("Patrol order:\n", patrol_queue)

# Remove the first boat (dequeue)
print("Next patrol completed by:", patrol_queue.popleft())

# Show updated queue
print("Remaining patrol order:\n", patrol_queue)

