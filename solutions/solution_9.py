# Prompt the user to enter the lower limit, upper limit, and the multiple.
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))
multiple = int(input("Enter the multiple: "))

# Loop through the range of the lower limit and upper limit and print the multiples of the multiple.
for i in range(lower_limit, upper_limit + 1):
    # Check if i is divisible by the multiple
    if i % multiple == 0:
        # If so, print i
        print(i, end=" ")
    else:
        # Otherwise, continue to the next iteration
        continue

print()
