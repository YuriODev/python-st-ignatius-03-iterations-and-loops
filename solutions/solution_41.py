# Prompt the user to enter an integer `n`.
n = int(input("Enter an integer: "))

# Initialize the first two numbers of the Fibonacci sequence.
a = 1
b = 1

# Initialize a variable to store the index of the current number in the Fibonacci sequence.
index = 2

# Iterate until the index of the current number in the Fibonacci sequence is less than `n`.
while index < n:
    # Update the first two numbers of the Fibonacci sequence.
    a, b = b, a + b

    # Increment the index by 1.
    index += 1

# Print the `n`-th number of the Fibonacci sequence.
print(b)
