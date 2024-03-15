# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Initialize a variable to store the total sum
total = 0

# Iterate through numbers from 1 to n-1
for i in range(1, n):
    # Calculate the product of i and (i + 1) and add it to the total
    total += i * (i + 1)

# Print the final total
print(total)
