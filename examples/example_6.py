# The variable to store the number of positive integers
positive = 0
# The variable to store the number of negative integers
negative = 0
# The variable to store the number of zeros
zeros = 0

# Prompt the user to enter the number of integers
n = int(input("Enter the number of integers: "))

# Iterate through the range of n to prompt the user to enter the numbers
for _ in range(n):
    # Prompt the user to enter the number
    number = int(input("Enter the number: "))
    # Check if the number is positive
    if number > 0:
        # Increment the positive variable
        positive += 1
    # Check if the number is negative
    elif number < 0:
        # Increment the negative variable
        negative += 1
    # If the number is zero
    else:
        # Increment the zeros variable
        zeros += 1

# Print the number of positive, negative, and zeros
print(positive, negative, zeros)
