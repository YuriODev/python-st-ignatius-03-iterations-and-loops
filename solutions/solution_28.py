# Prompt the user to enter two integers, `a` and `b`.
a = int(input())
b = int(input())

# Initialize the product
product = 0

# Calculate the product of a and b
# If both a and b are negative
if a < 0 and b < 0:
    # Convert them to positive and
    a = abs(a)
    b = abs(b)
    # Add b to the product a times.
    for i in range(a):
        product += b

# If a is negative
elif a < 0:
    # Convert a to positive
    a = abs(a)
    # Add a to the product b times.
    for i in range(a):
        product += b
    product = -product

# If b is negative
elif b < 0:
    # Convert b to positive
    b = abs(b)
    # Add b to the product a times.
    for i in range(b):
        product += a
    product = -product

# If both a and b are positive
else:
    # Add b to the product a times.
    for i in range(a):
        product += b

# Output the product  
print(product)
