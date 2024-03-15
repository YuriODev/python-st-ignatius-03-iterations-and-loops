# Initialize the count variable to keep track of the number of times a number is greater than the previous number
count = 0

# Prompt the user to enter the first number and convert it to an integer
previous = int(input("Enter the number: "))

# Start an infinite loop
while True:
    # Prompt the user to enter the next number and convert it to an integer
    number = int(input("Enter the number: "))

    # Check if the entered number is 0, which indicates the end of input
    if number == 0:
        break

    # Check if the entered number is greater than the previous number
    if number > previous:
        # If it is, increment the count variable
        count += 1

    # Update the previous variable with the current number for the next iteration
    previous = number

# Print the final count of numbers that were greater than the previous number
print(count)