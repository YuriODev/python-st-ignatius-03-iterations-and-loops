# Prompt the user to enter the number of days
n = int(input("Enter the number of days: "))

# Initialize the lowest temperature
lowest_temperature = 0

# Initialize the flag to check if the temperature has dropped below -18 degrees
below_negative_18 = False

# Loop through all the days
for i in range(n):
    # Prompt the user to enter the temperature for the day
    temperature = int(input("Enter the temperature for the day: "))

    # Update the lowest temperature
    if i == 0 or temperature < lowest_temperature:
        lowest_temperature = temperature

    # Check if the temperature has dropped below -18 degrees
    if temperature < -18:
        below_negative_18 = True

# Output the lowest temperature and whether the temperature has dropped below -18 degrees
print(lowest_temperature)

# Output "Yes" if the temperature has dropped below -18 degrees, otherwise output "No"
print("Yes" if below_negative_18 else "No")
