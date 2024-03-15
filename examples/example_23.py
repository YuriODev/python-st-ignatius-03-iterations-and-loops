# Prompt the user to enter the first number
a = int(input("Enter the first number: "))

# Prompt the user to enter the second number
b = int(input("Enter the second number: "))

# Create variables x and y to store the values of a and b respectively
x = a
y = b

# Calculate the product of a and b and store it in the variable 'product'
# because the value of a and b will be changed in the process of finding the gcd
product = abs(a * b)

# Solution 1: Using Euclidean algorithm to find the greatest common divisor (gcd)
while b:
    # Swap the values of a and b, and calculate the remainder of a divided by b
    a, b = b, a % b

# The gcd is stored in the variable 'a'
gcd = a

# Calculate the least common multiple (lcm) using the formula: lcm = abs(a * b) // gcd
lcm = product // gcd

# Print the lcm
print(lcm)

# Solution 2: Using a different non Pythonic approach to find the greatest common divisor (gcd)
while y != 0:
    # Store the value of y in a temporary variable
    temp = y

    # Calculate the remainder of x divided by y and assign it to y
    y = x % y

    # Assign the value of the temporary variable to x
    x = temp

# The gcd is stored in the variable 'x'
gcd = x

# Calculate the lcm using the formula: lcm = abs(a * b) // gcd
lcm = product // gcd

# Print the lcm
print(lcm)
