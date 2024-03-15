# Prompt the user to enter a number and convert it to an integer
n = int(input("Enter the number: "))  

# Iterate through the numbers from 10 to 99
for i in range(10, 100):  
    # Check if the number is odd and its last digit is equal to the input number
    if i % 2 != 0 and i % 10 == n:
        # Print the number if it satisfies the condition
        print(i, end=" ")
