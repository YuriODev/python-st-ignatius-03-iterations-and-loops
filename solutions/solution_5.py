# Prompt the user to enter a number
n = int(input())

# Calculate the sum of numbers from 1 to n using the formula (n * (n + 1)) // 2
total = 0

for i in range(1, n + 1):
    total += i

# Print the sum
print(total)
