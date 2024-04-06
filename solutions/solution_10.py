# Prompt the user to enter the number of pounds.
pounds = int(input())

# Initialize the kilograms variable.
kilograms = 0

# Loop through the range of pounds and print the equivalent kilograms.
for i in range(1, pounds + 1):
    kilograms += 0.453
    print(f"{i} {kilograms:.2f}")
