# Prompt the user to enter the first integer of the sequence.
number = int(input("Enter the first integer: "))

# Initialize the first and second largest elements of the sequence.
first_largest, second_largest = number, 0

# Prompt the user to enter the next integer of the sequence.
while number != 0:
    # Prompt the user to enter the next integer of the sequence.
    number = int(input(""))

    # Check if the current number is greater than the first largest element.
    if number > first_largest:
        # Update the second largest element.
        second_largest = first_largest

        # Update the first largest element.
        first_largest = number
    # Check if the current number is greater than the second largest element.
    elif number > second_largest:
        # Update the second largest element.
        second_largest = number

# Print the second largest element of the sequence.
print(second_largest)
