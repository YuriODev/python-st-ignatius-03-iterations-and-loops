# Prompt the user to enter the first integer of the sequence.
number = int(input("Enter the first integer: "))

# Initialize the largest element of the sequence.
largest = number

# Initialize the index of the largest element of the sequence.
index = 0

# Initialize the index of the current number in the sequence.
current_index = 0

# Prompt the user to enter the next integer of the sequence.
while number != 0:
    # Prompt the user to enter the next integer of the sequence.
    number = int(input(""))

    # Increment the index of the current number by 1.
    current_index += 1

    # Check if the current number is greater than the largest element.
    if number > largest:
        # Update the largest element.
        largest = number

        # Update the index of the largest element.
        index = current_index

# Print the index of the largest element of the sequence.
print(index)
