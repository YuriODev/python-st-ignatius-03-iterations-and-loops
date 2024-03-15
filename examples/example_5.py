# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Iterate from 1 to n (inclusive)
for i in range(1, n + 1):
    # Print the number i repeated i times
    print(str(i) * i)
