# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Iterate from 1 to n (inclusive)
for i in range(1, n + 1):
    # Iterate from i to n (inclusive)
    for j in range(i, n + 1):
        # Print the current value of j with a space as the separator
        print(j, end=" ")
    
    # Print a new line after each inner loop iteration
    print()
