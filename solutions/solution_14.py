# Prompting the user to enter the number of integers
n = int(input("Enter the number of integers: "))

# Initializing the count of zeros
count_of_zeros = 0

# Looping through the range of n
for i in range(n):
    # Prompting the user to enter the number
    number = int(input("Enter the number: "))

    # Checking if the number is equal to zero
    if number == 0:
        # Incrementing the count of zeros
        count_of_zeros += 1

# Printing the count of zeros
print(count_of_zeros)
