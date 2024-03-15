max_count = 0  # Maximum count of consecutive identical numbers
max_element = None  # Element with the maximum consecutive count
current_count = 1  # Current count of consecutive identical numbers
last_element = None  # Last seen element

# Input the first number
number = int(input("Enter a number (0 to end): "))
last_element = number

while number != 0:
    # Input next number
    number = int(input("Enter a number (0 to end): "))
    
    # Check if the current number is equal to the last number
    if number == last_element:
        current_count += 1  # Increment the current count
    else:
        # If the current streak ends, compare it to the maximum and update if necessary
        if current_count > max_count:
            max_count = current_count # Update the maximum count
            max_element = last_element # Update the maximum element
        current_count = 1  # Reset the current count for the new number
    
    last_element = number  # Update the last seen number

# Check the last sequence since it might be the max and wouldn't be checked in the loop
if current_count > max_count:
    max_count = current_count # Update the maximum count
    max_element = last_element # Update the maximum element

print(f"Longest sequence length: {max_count}")
if max_count > 0:  # Ensure there was at least one number before 0
    print(f"Most repeated element: {max_element}")
else:
    print("No numbers were entered before 0.")
