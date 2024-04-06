# Prompt the user to enter the number of rows in the pattern
rows = int(input("Enter the number of rows in the pattern: "))

# Iterate through the range of rows
for i in range(1, rows + 1):
    # Iterate through the range of numbers from 1 to i
    for j in range(1, i + 1):
        # Print the number j without a newline
        print(j, end="")
    # Print a newline after each row
    print()
