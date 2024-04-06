# Prompt the user to enter a number
number = int(input())

# Loop through all rows in the table
for i in range(number):
    # Loop through all columns in the table
    for j in range(number):
        # Check if the current row is equal to the current column
        if i == j:
            print("0", end="\t")
        # Check if the current row is above the main diagonal
        elif i < j:
            print("1", end="\t")
        # Check if the current row is below the main diagonal
        else:
            print("-1", end="\t")
    print()
else:
    print()
