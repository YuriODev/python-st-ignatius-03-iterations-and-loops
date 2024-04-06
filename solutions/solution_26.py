# Prompt the user to enter an integer, `n`.
n = int(input())

# Initialize the count of three-digit numbers
count = 0

# Calculate the number of three-digit numbers, the sum of the digits of which is equal to n
for i in range(100, 1000):

    # Extract the digits of the number
    first_digit = i // 100
    second_digit = i // 10 % 10
    third_digit = i % 10

    # Calculate the sum of the digits
    sum_of_digits = first_digit + second_digit + third_digit

    # Increment the count if the sum of the digits is equal to n
    if sum_of_digits == n:
        count += 1

# Output the count
print(count)
