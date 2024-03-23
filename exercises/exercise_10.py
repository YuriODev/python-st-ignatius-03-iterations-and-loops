
# ## Exercise 10: Pound to Kilogram Table - Easy 😊 (Est. Time: 10-15 mins | Points: 10)

# **Problem:** Write a program to print a table of equivalence between mass in pounds and mass in kilograms for the values of `n` pounds (1 pound = 453 grams) in the form of a table.

# ### Input:
# - An integer representing the number of pounds.

# ### Output:
# - A table of equivalence between mass in pounds and mass in kilograms for the values of `n` pounds.

# ### Examples:

# | No. | Inputs | Outputs |
# | --- | ------ | ------- |
# | 1   | 5      | 1 0.45<br>2 0.91<br>3 1.36<br>4 1.81<br>5 2.27 |
# | 2   | 3      | 1 0.45<br>2 0.91<br>3 1.36 |
# | 3   | 7      | 1 0.45<br>2 0.91<br>3 1.36<br>4 1.81<br>5 2.27<br>6 2.72<br>7 3.18 |

# ### Note:

# The problem tests the ability to use loops and conditional statements to print a table of values.

# Prompt the user to enter the number of pounds.
pounds = int(input())

# Initialize the kilograms variable.
kilograms = 0

# Loop through the range of pounds and print the equivalent kilograms.
for i in range(1, pounds + 1):
    kilograms += 0.45
    print(f"{i} {kilograms:.2f}")
