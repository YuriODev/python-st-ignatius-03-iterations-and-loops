# Prompt the user to enter a number
number = int(input())

# Loop through all integers formed from the input number
while number > 0:
    print(number)
    number //= 10
else:
    print(number)

# Output a newline character
print()
