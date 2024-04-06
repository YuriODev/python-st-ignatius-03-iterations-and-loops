# Prompt the user to enter two four-digit numbers `a` and `b`.
a = int(input("Enter the first four-digit number: "))
b = int(input("Enter the second four-digit number: "))

# We also need to take into consideration that a number can end up with 0

# Iterate through the range of integers from `a` to `b`.
for i in range(a, b + 1):
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
        # Print the palindrome.

        print(i, end=" ")
