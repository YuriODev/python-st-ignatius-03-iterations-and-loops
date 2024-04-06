# Prompt the user to enter two integers `a` and `b`.
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Initialize a variable to store the integer division of `a` by `b`.
division = 0

# Initialize a variable to store the remainder of the division of `a` by `b`.
remainder = 0

# Iterate until `a` is less than `b`.
while a >= b:
    # Subtract `b` from `a` and increment the division by 1.
    a -= b
    division += 1

# Set the remainder to the value of `a`.
remainder = a

# Print the results of the integer division of `a` by `b` and the remainder of the division of `a` by `b`.
print(division, remainder)
