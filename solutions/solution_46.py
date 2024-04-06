# Prompting the user to enter a natural number
number = int(input("Enter a natural number: "))

# Prompting the user to enter a digit
digit = int(input("Enter a digit: "))

# Looking for the position of the rightmost occurrence of the digit in the number
position = 0

# Iterating through the digits of the number
while number > 0:
    # Getting the last digit of the number
    last_digit = number % 10

    # Incrementing the position by 1
    position += 1

    # Checking if the last digit is equal to the digit
    if last_digit == digit:
        # Printing the position of the rightmost occurrence of the digit in the number
        print(position)

        # Exiting the loop
        break

    # Removing the last digit from the number
    number //= 10

# If the digit is not found in the number
if number == 0:
    # Printing 0
    print(0)
