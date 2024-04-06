# Prompt the user to enter the integer n.
n = int(input("Enter an integer: "))

# Initialize a variable to store the number of palindromes.
number_of_palindromes = 0

# Iterate through the range of integers from 1 to n.
for i in range(1, n + 1):
    # Check if the integer is a palindrome using loop

    # Initialize a variable to store the reversed integer.
    reversed_integer = 0

    # Initialize a variable to store the original integer.
    original_integer = i

    # Iterate until the original integer is not equal to 0.
    while original_integer != 0:
        # Get the last digit of the original integer.
        digit = original_integer % 10

        # Update the reversed integer.
        reversed_integer = reversed_integer * 10 + digit

        # Remove the last digit from the original integer.
        original_integer //= 10

    # Check if the reversed integer is equal to the original integer.
    if i == reversed_integer:
        # Increment the number of palindromes.
        number_of_palindromes += 1

# Print the number of palindromes.
print(number_of_palindromes)
