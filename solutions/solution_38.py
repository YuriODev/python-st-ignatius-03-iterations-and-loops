# Prompt the user to enter a number `n`.
n = int(input("Enter a number: "))

# Initialize a variable to store the maximum digit of `n`.
max_digit = 0

# Initialize a variable to store the minimum digit of `n`.
min_digit = 9

# Iterate over each digit of `n`.
while n > 0:
    # Get the last digit of `n`.
    digit = n % 10

    # Update the maximum digit if the current digit is greater than the current maximum digit.
    if digit > max_digit:
        max_digit = digit

    # Update the minimum digit if the current digit is less than the current minimum digit.
    if digit < min_digit:
        min_digit = digit

    # Remove the last digit from `n`.
    n //= 10

# Determine whether the difference between the maximum and minimum digits is even.
even_difference = (max_digit - min_digit) % 2 == 0

# Print the result.
print(even_difference)