# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Initialize variables
a = 0  # First number in the Fibonacci sequence
b = 1  # Second number in the Fibonacci sequence
c = 0  # Current number in the Fibonacci sequence
count = 0  # Counter to keep track of the position of the number in the Fibonacci sequence

# Loop until the current number in the Fibonacci sequence exceeds the input number
while c < n:
    # Calculate the next number in the Fibonacci sequence
    c = a + b
    # Update the values of a and b for the next iteration
    a = b
    b = c
    # Increment the counter
    count += 1

# Check if the input number is found in the Fibonacci sequence
if c == n:
    # If found, print the position of the number in the Fibonacci sequence
    print(count)
else:
    # If not found, print -1
    print(-1)
