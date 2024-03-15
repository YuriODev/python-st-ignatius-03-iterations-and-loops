# Prompt the user to enter the base
a = int(input("Enter the base: "))

# Prompt the user to enter the exponent
b = int(input("Enter the exponent: "))

# Initialize the result variable to 1
result = 1

# Perform the exponentiation using a loop
for _ in range(b):
    result *= a

# Print the result
print(result)
