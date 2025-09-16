coral_growth = [2.1, 2.5, 2.7, 3.0]  # cm/month
coral_growth.append(3.2)  # new growth data
print("Coral growth records:", coral_growth)

# Manual Index Print
print(coral_growth[0])

# Looped Index Print
print("\nCoral growth records (looped):")
for i in range(len(coral_growth)):
    print(f"Month {i+1}: {coral_growth[i]} cm")