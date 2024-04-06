# Prompt the user to enter a number
n = int(input())

# Iterate over the range from 2 to n (inclusive) with a step of 2
for i in range(2, n+1):
    # Check if i is even
    if i % 2 == 1:
        # If so, continue to the next iteration
        continue

    # Check if i is equal to n - 1 or n
    if i == n - 1 or i == n:
        # If so, print i
        print(i)
    else:
        # Otherwise, print i followed by a space (end=" ")
        print(i, end=" ")
