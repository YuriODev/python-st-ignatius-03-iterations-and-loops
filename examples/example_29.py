# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Iterate from 1 to n (inclusive)
for i in range(1, n + 1):
    # Initialize the count of divisors for each number
    divisors = 0
    
    # Iterate from 1 to i (inclusive) to check for divisors
    for j in range(1, i + 1):
        # Check if j is a divisor of i
        if i % j == 0:
            # If j is a divisor, increment the count of divisors
            divisors += 1
    
    # Print the number i along with '+' symbols representing the count of divisors
    print(f"{i}{'+' * divisors}")
