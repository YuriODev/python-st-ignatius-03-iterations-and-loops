# Prompt the user to enter a number
n = int(input("Enter the number: "))
temp_number = n

# Calculate the square of the number
square = n ** 2

# Count the number of digits in the number
digit_count = 0

# Calculate the number of digits in the square
while temp_number > 0:
    # Remove the last digit from the number
    temp_number //= 10
    # Increment the count of digits
    digit_count += 1

# Calculate the power of 10 based on the number of digits in the square
power = 10 ** digit_count

# Check if the last digit of the square is equal to the original number
if square % power == n:
    # Print True if the last digits of the square is equal to the original number
    print(True)
else:
    # Print False if the last digits of the square is not equal to the original number
    print(False)
