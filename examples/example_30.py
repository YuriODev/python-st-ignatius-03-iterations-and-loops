# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Create a temporary variable to store the original number
temp_number = n

# Initialize a variable to store the reversed number
reversed_number = 0

# Solution 1: Reversing the number using a while loop
while n > 0:
    # Extract the last digit of the number using the modulo operator
    last_digit = n % 10
    
    # Append the last digit to the reversed number by multiplying it by 10 and adding it
    reversed_number = reversed_number * 10 + last_digit
    
    # Remove the last digit from the number by integer division
    n //= 10

# Print the reversed number
print(reversed_number)

# Solution 2: Reversing the number using a while loop and power calculation
n = temp_number
power = 0

# Calculate the number of digits in the original number
while temp_number > 0:
    # Remove the last digit from the temporary number
    temp_number //= 10
    
    # Increment the power variable to keep track of the number of digits
    power += 1

# Reset the reversed number variable
reversed_number = 0

# Reconstruct the reversed number by multiplying each digit with the appropriate power of 10
while n > 0:
    # Extract the last digit of the number using the modulo operator
    current_digit = n % 10
    
    # Calculate the number to add to the reversed number by multiplying the current digit with the appropriate power of 10
    number_to_add = current_digit * (10 ** (power - 1))
    
    # Add the number to add to the reversed number
    reversed_number += number_to_add
    
    # Remove the last digit from the number by integer division
    n //= 10
    
    # Decrement the power variable to adjust for the next digit
    power -= 1

# Print the reversed number
print(reversed_number)
