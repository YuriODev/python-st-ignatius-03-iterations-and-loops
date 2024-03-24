# # ## Exercise 22: Number Pattern - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

# # **Problem:** Write a program to print all integers formed from the input number by discarding the last digit from each previous number.

# # ### Input:

# # - An integer representing the input number.

# # ### Output:

# # - A sequence of integers formed from the input number by discarding the last digit from each previous number.

# # ### Examples:

# # | No. | Inputs | Outputs |
# # | --- | ------ | ------- |
# # | 1   | 138945 | 13894<br> 1389<br> 138<br> 13<br> 1 |
# # | 2 | 123456 | 12345<br> 1234<br> 123<br> 12<br> 1 |
# # | 3 | 987654 | 98765<br> 9876<br> 987<br> 98<br> 9 |

# # Your solution to Exercise 22

# # Prompt the user to enter a number
# number = int(input())

# # Loop through all integers formed from the input number
# while number > 0:
#     print(number, end="\n")
#     number //= 10

# # Output a newline character
# print()


import unittest
from .test_utils import CustomTestCase, CustomTestRunner

class TestExercise22(unittest.TestCase):
    


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
