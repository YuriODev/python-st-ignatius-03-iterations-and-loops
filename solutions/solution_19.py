# Prompt the user to enter a number
number = int(input())

# Loop through all two-digit numbers
for i in range(10, 100):
    # Calculate the sum of the squares of the digits
    sum_of_squares = (i // 10) ** 2 + (i % 10) ** 2

    # Check if the sum is divisible by the input number
    if sum_of_squares % number == 0:
        print(i, end=", ")

# Output a newline character
print()
