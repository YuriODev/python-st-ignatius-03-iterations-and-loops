# Prompt the user to enter a number
n = int(input())

# Iterate from 1 to n (inclusive)
for i in range(1, n+1):
    # Print a line of characters
    # The line consists of a "#" followed by (i-1) spaces and another "#"
    print("#" + " " * (i-1) + "#")
