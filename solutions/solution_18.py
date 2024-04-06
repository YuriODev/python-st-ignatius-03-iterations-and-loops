# ## Exercise 18: Number Pattern - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

# **Problem:** Write a program to determine the total number of erors collected over `n` days.

# ### Input:
# - An integer `n` representing the number of days.
# - `n` integers representing the number of errors collected each day.

# ### Output:
# - An integer representing the total number of errors collected over `n` days.

# ### Examples:

# | No. | Inputs | Outputs |
# | --- | ------ | ------- |
# | 1   | 6<br>45<br>101<br>67<br>43<br>21<br>0 | 277 |
# | 2   | 3<br>0<br>0<br>0 | 0 |
# | 3   | 5<br>1<br>2<br>3<br>4<br>5 | 15 |

# Solution

# Prompt the user to enter the number of days
days = int(input())

# Initialize a variable to store the total number of errors
total_errors = 0

# Iterate over the range of days
for _ in range(days):
    # Prompt the user to enter the number of errors collected each day
    errors = int(input())
    # Add the number of errors collected each day to the total_errors
    total_errors += errors

# Print the total number of errors collected over n days
print(total_errors)
