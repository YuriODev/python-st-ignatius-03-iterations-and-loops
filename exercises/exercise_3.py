# Prompt the user to enter a number
n = int(input())

# Iterate over a range of numbers from 20 to n+1
for i in range(20, n+1):
    # Check if the current number is equal to n
    if i == n:
        # If it is, print the number
        print(i)
    else:
        # If it's not, print the number followed by a space
        print(i, end=" ")
