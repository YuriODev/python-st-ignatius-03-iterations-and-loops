# Prompt the user to enter two four-digit numbers `a` and `b`.
a = int(input("Enter the first four-digit number: "))
b = int(input("Enter the second four-digit number: "))

# Iterate through the range of integers from `a` to `b` to find numbers with 3 
# identical digits at any positions
for i in range(a, b):
    # Check if the integer has 3 identical digits at any positions using loop

    # Initialize a variable to store the original integer.
    original_integer = i

    # Get all 4 digits of the original integer.
    digit_thousands = original_integer % 10
    digit_hundreds = original_integer // 10 % 10
    digit_tens = original_integer // 100 % 10
    digit_units = original_integer // 1000

    # Check if the integer has 3 identical digits at any positions.
    if digit_thousands == digit_hundreds == digit_tens or \
       digit_thousands == digit_hundreds == digit_units or \
       digit_thousands == digit_tens == digit_units or \
       digit_hundreds == digit_tens == digit_units:
        # Print the integer.
        print(i, end=" ")
