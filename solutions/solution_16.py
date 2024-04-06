# Prompting the user to enter the number of steps in the staircase
n = int(input("Enter the number of steps in the staircase: "))

# Looping through the range of n
for i in range(n):
    # Printing the spaces
    print(" " * (n - i - 1), end="")
    
    # Printing the hashes
    print("#" * (i + 1))
