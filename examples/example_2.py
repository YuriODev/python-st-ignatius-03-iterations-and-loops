# Prompt the user to enter the first number
a = int(input("Enter the first number: "))

# Prompt the user to enter the second number
b = int(input("Enter the second number: "))

# Check if the first number is less than or equal to the second number
if a <= b:
    # If true, iterate from the first number to the second number (inclusive)
    for i in range(a, b + 1):
        # Print each number in the range, separated by a space
        print(i, end=" ")
else:
    # If false, iterate from the first number to the second number (inclusive) in reverse order
    for i in range(a, b - 1, -1):
        # Print each number in the range, separated by a space
        print(i, end=" ")
