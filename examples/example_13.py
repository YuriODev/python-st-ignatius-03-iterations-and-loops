n = int(input("Enter the number of integers: "))

# Initialize a variable to store the sum of the integers
total = 0

# Iterate 'n' times to get 'n' integers from the user
for _ in range(n):
    # Prompt the user to enter an integer and add it to the total
    total += int(input("Enter the number: "))

# Print the sum of the integers
print(total)
