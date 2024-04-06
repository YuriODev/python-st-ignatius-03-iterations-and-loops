# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Loop through all odd numbers from 1 to the input number

for i in range(1, number + 1, 2):
    print(i, end=" ")
print()
