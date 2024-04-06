# Prompt the user to enter two integers, `d` and `t`.
d = int(input())
t = int(input())

# Initialize the distance covered and the number of days
distance_covered = d

# Initialize the number of days
days = 1

# Calculate the distance covered and the number of days
while distance_covered <= t:
    distance_covered += d + (d * 0.1)
    d += (d * 0.1)
    days += 1

# Output the distance covered and the number of days
print(f"{distance_covered:.2f} km, {days} days")
