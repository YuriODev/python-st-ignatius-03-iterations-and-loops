# Initialize variables to keep track of the maximum number and its count
max_number = 0  # The maximum number encountered so far
max_count = 0  # The count of occurrences of the maximum number

# Start an infinite loop
while True:
    # Prompt the user to enter a number
    number = int(input("Enter the number: "))

    # Check if the entered number is 0
    if number == 0:
        break  # If the number is 0, exit the loop

    # Check if the entered number is greater than the current maximum number
    if number > max_number:
        max_number = number  # If so, update the maximum number
        max_count = 1  # Reset the count to 1 since we have encountered a new maximum
    # Check if the entered number is equal to the current maximum number
    elif number == max_number:
        max_count += 1  # If so, increment the count of occurrences of the maximum number

# Print the final count of occurrences of the maximum number
print(max_count)
