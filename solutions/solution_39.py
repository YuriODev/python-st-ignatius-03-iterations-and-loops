# Prompting the user to enter an integer
n = abs(int(input()))

# Initializing a variable to store the sum of the digits of `n`
sum_of_digits = 0

# Iterating over each digit of `n`
while n != 0:
    # print(f"{n = }")
    # Getting the last digit of `n`
    digit = n % 10

    # Adding the digit to the sum
    sum_of_digits += digit

    # Removing the last digit from `n`
    n //= 10

# Printing the sum of the digits of `n`
print(sum_of_digits)
