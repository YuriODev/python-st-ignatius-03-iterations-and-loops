# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Iterate through the range from 1 to 10 (inclusive)
for i in range(1, 11):
    # Multiply the number entered by the current iteration value and print the result
    print(f"{n} x {i} = {n * i}")
