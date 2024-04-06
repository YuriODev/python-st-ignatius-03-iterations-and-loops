# Prompt the user to enter two integers separated by a space.
# The first integer represents the number of rows `n` and the second integer
# represents the number of columns `m`. Print the pattern as shown in
# the examples.

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

for i in range(n):
    print(f"{i}\t" * m)
