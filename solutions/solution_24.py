# Prompt the user to enter a number
number = int(input())

# Initialize the count of even elements in the sequence
count = 0

# Loop through all integers in the sequence
while number != 0:
    if number % 2 == 0:
        count += 1
    number = int(input())

# Output the number of even elements in the sequence
print(count)
