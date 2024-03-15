# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Initialize a variable to keep track of the count
count = 0

# Execute the loop as long as the number is greater than 0
while n > 0:
    n //= 10  # Decrease the number by one digit by integer division
    count += 1  # Increase the count by one

# Print the final count
print(count)
