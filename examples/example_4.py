# Prompt the user to enter a number and convert it to an integer
n = int(input("Enter the number: "))  

# Loop from n to 0 (inclusive), with a step of -1
for i in range(n, -1, -1):
    # Print the current value of i and a string of "#" characters multiplied by i
    print(i, "#" * i)  
