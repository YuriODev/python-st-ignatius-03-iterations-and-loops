# # ## Exercise 28: Product of Two Numbers - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

# # **Problem:** Given integers a and b. Find their product without using the multiplication operation.

# # ### Input:

# # - Two integers `a` and `b`.

# # ### Output:

# # - An integer representing the product of `a` and `b`.

# # ### Examples:

# # | No. | Inputs | Outputs |
# # | --- | ------ | ------- |
# # | 1   | 7<br> 8 | 56 |
# # | 2 | 5<br> 6 | 30 |
# # | 3 | 3<br> 4 | 12 |
# # | 4 | 10<br> 10 | 100 |

# # ### Note:

# # The problem tests the ability to use loops and conditional statements to calculate the product of two numbers.

# # Your solution to Exercise 28

# # Prompt the user to enter two integers, `a` and `b`.
# a = int(input())
# b = int(input())

# # Initialize the product
# product = 0

# # Calculate the product of a and b
# # If both a and b are negative
# if a < 0 and b < 0:
#     # Convert them to positive and
#     a = abs(a)
#     b = abs(b)
#     # Add b to the product a times.
#     for i in range(a):
#         product += b

# # If a is negative
# elif a < 0:
#     # Convert a to positive
#     a = abs(a)
#     # Add a to the product b times.
#     for i in range(a):
#         product += b
#     product = -product

# # If b is negative
# elif b < 0:
#     # Convert b to positive
#     b = abs(b)
#     # Add b to the product a times.
#     for i in range(b):
#         product += a
#     product = -product

# # If both a and b are positive
# else:
#     # Add b to the product a times.
#     for i in range(a):
#         product += b

# # Output the product  
# print(product)

import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise28(CustomTestCase):
    
    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_no_asterisk(self):
        """
        The program should not use the multiplication operation to calculate the product of two numbers.
        """

        self.assertNoProductSymbolUsage()

    def test_product_of_two_numbers(self):
        """
        The program should prompt the user to enter two integers, `a` and `b`, and output their product without using the multiplication operation.
        """

        inputs = ["7", "8"]
        output = self.run_exercise(inputs)
        expected_output = "56\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_product_of_two_numbers_2(self):
        """
        The program should prompt the user to enter two integers, `a` and `b`, and output their product without using the multiplication operation.
        """

        inputs = ["5", "6"]
        output = self.run_exercise(inputs)
        expected_output = "30\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_product_of_two_numbers_3(self):
        """
        The program should prompt the user to enter two integers, `a` and `b`, and output their product without using the multiplication operation.
        """

        inputs = ["3", "4"]
        output = self.run_exercise(inputs)
        expected_output = "12\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_product_of_two_numbers_4(self):
        """
        The program should prompt the user to enter two integers, `a` and `b`, and output their product without using the multiplication operation.
        """

        inputs = ["10", "10"]
        output = self.run_exercise(inputs)
        expected_output = "100\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs) 
        

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())