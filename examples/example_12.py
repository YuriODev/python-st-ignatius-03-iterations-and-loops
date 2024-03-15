# Prompt the user to enter the first number
n = int(input("Enter the number: "))

# Start an infinite loop
while True:
    # Prompt the user to enter a number
    number = int(input("Enter the number: "))

    # Check if the entered number is equal to the first number
    if number == n:
        # If the numbers are equal, print "Done"
        print("Done")
        # Exit the loop
        break
