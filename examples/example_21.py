# Prompt the user to enter the number of cars
n = int(input("Enter the number of cars: "))

# Initialize variables
total_speed = 0
over_speed = False

# Iterate 'n' times to get the speed of each car
for _ in range(n):
    speed = int(input("Enter the speed: "))
    total_speed += speed
    if speed > 60:
        over_speed = True

# Calculate the average speed
average_speed = total_speed / n

# Print the average speed with one decimal place
print(f"{average_speed:.1f}")

# Print "Yes" if any car was over the speed limit, otherwise print "No"
print("Yes" if over_speed else "No")
