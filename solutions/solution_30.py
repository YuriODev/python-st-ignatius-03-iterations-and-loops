# Prompting the user to enter the number of hours
t = int(input("Enter the number of hours: "))

# Initializing the number of cells at the start
cells = 1

# Initializing the time counter
hours_passed = 0

# Looping until the total hours have passed
while hours_passed < t:
    # Every 3 hours, double the number of cells
    if (hours_passed + 1) % 3 == 0:
        cells *= 2
    # Increment the hours passed
    hours_passed += 1

# Displaying the number of cells
print(cells)
