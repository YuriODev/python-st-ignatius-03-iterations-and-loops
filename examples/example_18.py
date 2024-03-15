# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Initialize a variable to store the sum of digits
digits_total = 0

# Iterate through numbers from 100 to 999
for i in range(100, 1000):
    current_number = i
    digits_total = 0
    
    # Calculate the sum of digits in the current number
    while current_number > 0:
        # Add the last digit to the sum of digits
        digits_total += current_number % 10
        # Remove the last digit from the current number
        current_number //= 10

    # Check if the sum of digits matches the user input
    if digits_total == n:
        # Print the number if the sum of digits matches
        print(i, end=" ")
