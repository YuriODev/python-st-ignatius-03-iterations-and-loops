# Prompt the user to enter two integers `a` and `b`.
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Find previous odd number for `a` without using IF statement
a -= a % 2 == 0

# Iterate until `a` is less than or equal to `b`.
while a >= b:
    # Print the odd number.
    print(a, end=" ")
    # Update `a` to the next odd number.
    a -= 2
