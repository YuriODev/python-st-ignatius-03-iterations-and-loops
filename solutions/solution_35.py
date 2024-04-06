# Prompt the user to enter an integer `n`.
n = int(input("Enter an integer: "))

# Initialize a variable to store the maximum number of digits
max_digits = 10 ** n

# Iterate through the range of numbers from 1 to `max_digits`
for i in range(max_digits - 1, 10 ** (n - 1) - 1, -2):
    # Print the number `i` without a newline
    print(i, end=" ")

# Print a newline after printing all the numbers
print()
