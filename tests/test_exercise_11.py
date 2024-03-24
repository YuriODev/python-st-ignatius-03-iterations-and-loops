# # ## Exercise 11: Sum of a Series - Easy 😊 (Est. Time: 5 mins | Points: 10)

# # **Problem:** Write a program to calculate the sum of the expression `1/2 + 2/3 + 3/4 + …​ + n/(n + 1)` for a given value of `n`.

# # ### Input:
# # - An integer representing the upper limit of the range.

# # ### Output:
# # - A floating-point number representing the sum of the expression `1/2 + 2/3 + 3/4 + …​ + n/(n + 1)`.

# # ### Examples:

# # | No. | Inputs | Outputs |
# # | --- | ------ | ------- |
# # | 1   | 5      | 3.55 |
# # | 2   | 10     | 7.98 |
# # | 3   | 3      | 1.92 |

# # ### Note:

# # The problem tests the ability to use loops and conditional statements to calculate the sum of a series.


# # Your solution to Exercise 11

# # Prompting the user to enter the upper limit of the range
# n = int(input("Enter the upper limit of the range: "))

# # Initializing the sum of the series
# sum_of_series = 0

# # Looping through the range of 1 to n
# for i in range(1, n + 1):
#     # Calculating the sum of the series
#     sum_of_series += i / (i + 1)

# # Printing the sum of the series
# print(sum_of_series)

import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise11(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_sum_of_series_5(self):
        """
        The program should calculate the sum of the series up to 5.
        """

        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "3.55\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_series_10(self):
        """
        The program should calculate the sum of the series up to 10.
        """

        inputs = ["10"]
        output = self.run_exercise(inputs)
        expected_output = "7.98\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_series_3(self):
        """
        The program should calculate the sum of the series up to 3.
        """

        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "1.92\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_series_1(self):
        """
        The program should calculate the sum of the series up to 1.
        """

        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "0.50\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_series_2(self):
        """
        The program should calculate the sum of the series up to 2.
        """

        inputs = ["2"]
        output = self.run_exercise(inputs)
        expected_output = "1.17\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
