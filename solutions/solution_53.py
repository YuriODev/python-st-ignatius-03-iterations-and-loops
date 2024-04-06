# ## Exercise 53: Even Numbers - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

# **Problem:** Two numbers `a` and `b` are entered. Print all even numbers from the interval from `a` to `b` (a ≤ b). Write a program without using a branching instruction.

# ### Input:

# - Two integers `a` and `b` (a ≤ b).

# ### Output:

# - A sequence of even numbers from the interval from `a` to `b`.

# ### Examples:

# | No. | Inputs | Outputs |
# | --- | ------ | ------- |
# | 1   | 1<br>20 | 2 4 6 8 10 12 14 16 18 20 |
# | 2   | 1<br>30 | 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 |
# | 3   | 1<br>40 | 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 |


# Your solution to Exercise 53

# Prompt the user to enter two integers `a` and `b`.
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Find next even number for `a` without using IF statement
a += a % 2 == 1

# Iterate until `a` is less than or equal to `b`.
while a <= b:
    # Print the even number.
    print(a, end=" ")
    # Update `a` to the next even number.
    a += 2
