# Prompting the user to enter the number n
n = int(input("Enter the number n: "))

# Initializing the sum of the three-digit numbers
sum_of_three_digit_numbers = 0

# Looping through the range of 100 to 999
for i in range(100, 1000):
    # Checking if the number is divisible by n
    if i % n == 0:
        # Adding the number to the sum of the three-digit numbers
        sum_of_three_digit_numbers += i

# Printing the sum of the three-digit numbers
print(sum_of_three_digit_numbers)
