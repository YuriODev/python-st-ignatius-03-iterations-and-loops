# Prompting the user to enter the first number of the sequence.
number = int(input("Enter the first number of the sequence: "))

# Initialize a variable to store the count of numbers that are greater than the next element.
count = 0

# Initialize a variable to store the previous number in the sequence.
previous = number

# Prompt the user to enter the next number of the sequence.
while number != 0:
    # Prompt the user to enter the next number of the sequence.
    number = int(input(""))

    # Check if the current number is greater than the previous number.
    if number < previous:
        # Increment the count by 1.
        count += 1

    # Update the previous number.
    previous = number

# Print the count of numbers that are greater than the next element.
print(count)
