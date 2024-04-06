# Prompt the user to enter the number of recorded cars
n = int(input("Enter the number of recorded cars: "))

# Initialize the maximum and minimum speeds of the cars
max_speed = 0
min_speed = 300

# Initialize the number of cars whose speed did not exceed 30 km/h
cars_below_30 = 0

# Loop through all recorded cars
for i in range(n):
    # Prompt the user to enter the speed of the car
    speed = int(input("Enter the speed of the car: "))

    # Update the maximum speed of the cars
    if speed > max_speed:
        max_speed = speed
    
    # Update the minimum speed of the cars
    if speed < min_speed:
        min_speed = speed

    # Update the number of cars whose speed did not exceed 30 km/h
    if speed <= 30:
        cars_below_30 += 1

# Calculate the difference between the maximum and minimum speeds of the cars
difference = max_speed - min_speed

# Output the difference between the maximum and minimum speeds of the cars
print(difference)

# Output the number of cars whose speed did not exceed 30 km/h
print(cars_below_30)
