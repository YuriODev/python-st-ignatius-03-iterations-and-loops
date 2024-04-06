# Read the first number
number = int(input())

# Initialize the total
total = number

# Initialize the sum of squares
sum_of_squares = number ** 2

# Continue reading numbers until the sum of the entered numbers equals 0
while total != 0:
    number = int(input())
    sum_of_squares += abs(number) ** 2
    total += number

# Output the sum of the squares of all the entered numbers
print(sum_of_squares)
