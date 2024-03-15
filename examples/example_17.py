# Initialize the maximum number to 0
max_number = 0

# Start an infinite loop
while True:
    # Prompt the user to enter a number
    number = int(input("Enter the number: "))

    # Check if the entered number is 0
    if number == 0:
        # If it is, break out of the loop
        break

    # Check if the entered number is greater than the current maximum number
    if number > max_number:
        # If it is, update the maximum number
        max_number = number

# Print the maximum number
print(max_number)
