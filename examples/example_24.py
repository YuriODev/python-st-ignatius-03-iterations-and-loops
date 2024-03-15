# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Initialize variables
i = 1  # Represents the current number to be printed
count = 0  # Represents the count of numbers printed so far

# Loop until count reaches the input number
while count < n:
    # Loop 'i' times to print the current number 'i'
    for _ in range(i):
        # Check if count is still less than the input number
        if count < n:
            # Print the current number without a new line
            print(i, end=" ")
            # Increment the count of numbers printed
            count += 1
    # Increment the current number to be printed
    i += 1
