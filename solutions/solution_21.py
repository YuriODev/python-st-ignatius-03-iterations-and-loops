# Prompt the user to enter a number
number = int(input())

# Initialize the sum of factorials
sum_of_factorials = 0

# Loop through all integers from 1 to the input number
for i in range(1, number + 1):
    # Initialize the factorial of the current number
    factorial = 1

    # Calculate the factorial of the current number
    for j in range(1, i + 1):
        factorial *= j

    # Add the factorial to the sum
    sum_of_factorials += factorial

# Output the sum of factorials
print(sum_of_factorials)
