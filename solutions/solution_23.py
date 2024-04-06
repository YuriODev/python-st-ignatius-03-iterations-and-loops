# Prompt the user to enter a number
number = int(input())

if number == 0:
    # If the first number is 0, output 0 and end the program
    print(0)

else:
    # Initialize the sum of all integers in the sequence
    total = 0

    # Initialize the count of all integers in the sequence
    count = 0

    # Loop through all integers in the sequence
    while number != 0:
        total += number
        count += 1
        number = int(input())

    # Calculate the average of all integers in the sequence
    average = total / count

    # Output the average of all integers in the sequence
    print(average)
