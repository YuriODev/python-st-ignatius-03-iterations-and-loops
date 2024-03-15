# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Initialize variables to count the occurrences of each power of 2
ones = 0
twos = 0
fours = 0
eights = 0
sixteens = 0
thirty_twos = 0
sixty_fours = 0

# Iterate until the number becomes 0
while n > 0:
    # Check if the number is greater than or equal to 64
    if n >= 64:
        sixty_fours += 1  # Increment the count of 64s
        n -= 64  # Subtract 64 from the number
    # Check if the number is greater than or equal to 32
    elif n >= 32:
        thirty_twos += 1  # Increment the count of 32s
        n -= 32  # Subtract 32 from the number
    # Check if the number is greater than or equal to 16
    elif n >= 16:
        sixteens += 1  # Increment the count of 16s
        n -= 16  # Subtract 16 from the number
    # Check if the number is greater than or equal to 8
    elif n >= 8:
        eights += 1  # Increment the count of 8s
        n -= 8  # Subtract 8 from the number
    # Check if the number is greater than or equal to 4
    elif n >= 4:
        fours += 1  # Increment the count of 4s
        n -= 4  # Subtract 4 from the number
    # Check if the number is greater than or equal to 2
    elif n >= 2:
        twos += 1  # Increment the count of 2s
        n -= 2  # Subtract 2 from the number
    else:
        ones += 1  # Increment the count of 1s
        n -= 1  # Subtract 1 from the number

# Print the counts of each power of 2, if they are greater than 0
if sixty_fours > 0:
    print(f"{sixty_fours} (64)")

if thirty_twos > 0:
    print(f"{thirty_twos} (32)")

if sixteens > 0:
    print(f"{sixteens} (16)")

if eights > 0:
    print(f"{eights} (8)")

if fours > 0:
    print(f"{fours} (4)")

if twos > 0:
    print(f"{twos} (2)")

if ones > 0:
    print(f"{ones} (1)")
