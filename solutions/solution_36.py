# Prompt the user to enter two integers `a` and `b`.
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Initialize a variable to store the remainder of the division of `a` by `b`.
remainder = a % b

# Iterate until the remainder is not equal to 0.
while remainder != 0:
    # Set `a` to `b` and `b` to the remainder.
    a = b
    b = remainder
    # Update the remainder.
    remainder = a % b

# Print the greatest common divisor.
print(b)
