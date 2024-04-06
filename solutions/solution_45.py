# Prompt the user to enter the first number of the sequence.
n = int(input("Enter a number: "))

# Initialize the number of sign changes in the sequence.
sign_changes = 0

# Initialize the sign of the current number in the sequence.
sign = 1 if n > 0 else -1

# Prompt the user to enter the next number of the sequence.
while n != 0:
    # Prompt the user to enter the next number of the sequence.
    n = int(input(""))

    # Check if the sign of the current number is different from the sign of the previous number.
    if sign * n < 0:
        # Increment the number of sign changes by 1.
        sign_changes += 1

        # Update the sign of the current number.
        sign = -sign

# Print the number of sign changes in the sequence.
print(sign_changes)
