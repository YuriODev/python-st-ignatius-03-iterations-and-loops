# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Initialize the factorial variable to 1
factorial = 1

# Iterate from 1 to n (inclusive)
for i in range(1, n + 1):
    # Multiply the current value of factorial by i
    factorial *= i

# Print the factorial
print(factorial)
