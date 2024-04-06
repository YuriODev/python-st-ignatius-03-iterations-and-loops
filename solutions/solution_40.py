# Prompt the user to enter an integer `n`.
n = int(input("Enter an integer: "))

# Initialize the first two numbers of the Fibonacci sequence.
a = 1
b = 1

# Print the first number of the Fibonacci sequence.
print(a, end=" ")

# Iterate until the sum of the last two numbers of the Fibonacci sequence is less than `n`.
while a + b < n:
    # Print the next number of the Fibonacci sequence.
    print(b, end=" ")

    # Update the first two numbers of the Fibonacci sequence.
    a, b = b, a + b

# Print the last number of the Fibonacci sequence.
print(b)
