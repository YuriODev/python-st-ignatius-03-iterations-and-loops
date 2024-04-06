# ## Exercise 13: Password Validation - Easy 😊 (Est. Time: 5 mins | Points: 10)

# **Problem:** Write a program to prompt the user for a password. If the user enters the wrong password, the program should display an error message and prompt the user to try again. If the user enters the correct password, the program should display a success message.

# ### Input:
# - An integer representing the password.
# - A sequence of integers representing the password entered by the user.

# ### Output:
# - A message indicating whether the password is correct or incorrect.

# ### Examples:

# | No. | Inputs | Outputs |
# | --- | ------ | ------- |
# | 1   | 12345  | 111<br>Error<br>45<br>Error<br>12345<br>Done |
# | 2   | 123    | 111<br>Error<br>45<br>Error<br>12345<br>Error |
# | 3   | 111    | 111<br>Done |

# ### Note:

# The problem tests the ability to use loops and conditional statements to validate user input.

# Prompt the user to enter the password.
password = int(input("Enter the password: "))

# Initialize the user_password variable.
user_password = 0

# Loop until the user enters the correct password.
while user_password != password:
    user_password = int(input("Enter the password: "))
    if user_password != password:
        print("Error")
    else:
        print("Done")
