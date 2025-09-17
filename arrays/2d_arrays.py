# 2D Array Example: Temperatures of 3 cities over 7 days
temperatures = [
    [30, 31, 29, 32, 33, 31, 30],  # City A
    [25, 26, 27, 26, 28, 27, 25],  # City B
    [20, 21, 19, 22, 23, 21, 20]   # City C
]

# Manual
print(temperatures[2][1])

# Looped
print("Temperature Records (°C):")
for i in range(len(temperatures)):
    print(f"City {i+1}: ", end="")
    for j in range(len(temperatures[i])):
        print(temperatures[i][j], end=" ")
    print()


