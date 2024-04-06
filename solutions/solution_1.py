# Prompt the user to enter a number
number = int(input())

# Iterate over a range of numbers from number-1 down to 1 (excluding 0)
for i in range(number, 0, -1):
    # Print each number in the range
    print(i)

# Print "Start!" after the loop completes
print("Start!")
