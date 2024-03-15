# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Iterate from 1 to n (inclusive)
for i in range(1, n + 1):
    # Check if the current number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("*35*")  # Print *35* if divisible by both 3 and 5
    # Check if the current number is divisible by 3 only
    elif i % 3 == 0:
        print("*3*")  # Print *3* if divisible by 3 only
    # Check if the current number is divisible by 5 only
    elif i % 5 == 0:
        print("*5*")  # Print *5* if divisible by 5 only
    else:
        print(i)  # Print the current number if not divisible by 3 or 5
