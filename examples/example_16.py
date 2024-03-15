# Initialize the total variable
total = 0

# Start an infinite loop
while True:
    # Prompt the user to enter a number
    number = int(input("Enter the number: "))

    # Check if the entered number is 0
    if number == 0:
        # If the number is 0, exit the loop
        break

    # Add the entered number to the total
    total += number

# Print the final total
print(total)
