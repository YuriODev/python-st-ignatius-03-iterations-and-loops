# Prompt the user to enter the number of terms in the series.
n = int(input("Enter the number of terms in the series: "))

# Initialize the sum of the series
sum_of_series = 0

# Initialize the sign
sign = 1

# Calculate the sum of the series
for i in range(1, n + 1, 2):
    sum_of_series += sign * 4 / i
    sign *= -1

# Output the sum of the series
print(f"{sum_of_series:.16f}")
