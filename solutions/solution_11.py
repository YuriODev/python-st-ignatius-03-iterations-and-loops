# Prompting the user to enter the upper limit of the range
n = int(input("Enter the upper limit of the range: "))

# Initializing the sum of the series
sum_of_series = 0

# Looping through the range of 1 to n
for i in range(1, n + 1):
    # Calculating the sum of the series
    sum_of_series += i / (i + 1)

# Printing the sum of the series
print(f"{sum_of_series:.2f}")