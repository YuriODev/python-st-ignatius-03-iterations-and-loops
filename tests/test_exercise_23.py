
# # ## Exercise 23: Average of a Sequence - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

# # **Problem:** Write a program to calculate the average of all integers in a sequence that ends with the number `0`. The number `0` is not included in the sequence, but is used as a sign of its end.

# # ### Input:

# # - A sequence of integers that ends with the number `0`.

# # ### Output:

# # - A floating-point number representing the average of all integers in the sequence.

# # ### Examples:

# # | No. | Inputs | Outputs |
# # | --- | ------ | ------- |
# # | 1   | 3<br>4<br>5<br>0 | 4.0 |
# # | 2 | 1<br>2<br>3<br>4<br>5<br>0 | 3.0 |
# # | 3 | 10<br>20<br>30<br>40<br>50<br>0 | 30.0 |

# # ### Note:

# # The problem tests the ability to use loops and conditional statements to calculate the average of a sequence of numbers.

# # Your solution to Exercise 23

# # Prompt the user to enter a number
# number = int(input())

# # Initialize the sum of all integers in the sequence
# total = 0

# # Initialize the count of all integers in the sequence
# count = 0

# # Loop through all integers in the sequence
# while number != 0:
#     total += number
#     count += 1
#     number = int(input())

# # Calculate the average of all integers in the sequence
# average = total / count

# # Output the average of all integers in the sequence
# print(average)


import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise23(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()


    def test_3_4_5_0(self):
        """
        The program should print the average of all integers in the sequence [3, 4, 5].
        """

        inputs = ["3", "4", "5", "0"]
        output = self.run_exercise(inputs)
        expected_output = "4.0\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_1_2_3_4_5_0(self):
        """
        The program should print the average of all integers in the sequence [1, 2, 3, 4, 5].
        """

        inputs = ["1", "2", "3", "4", "5", "0"]
        output = self.run_exercise(inputs)
        expected_output = "3.0\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_10_20_30_40_50_0(self):
        """
        The program should print the average of all integers in the sequence [10, 20, 30, 40, 50].
        """

        inputs = ["10", "20", "30", "40", "50", "0"]
        output = self.run_exercise(inputs)
        expected_output = "30.0\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_1_2_3_4_5_6_7_8_9_10_0(self):

        """
        The program should print the average of all integers in the sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
        """

        inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "0"]
        output = self.run_exercise(inputs)
        expected_output = "5.5\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_1_0(self):
        """
        The program should print the average of all integers in the sequence [1].
        """

        inputs = ["1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "1.0\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_no_division_by_zero(self):
        """
        The program should not divide by zero.
        """

        inputs = ["0"]
        try:
            output = self.run_exercise(inputs)
            expected_output = "0\n"
            self.assertInCustom(expected=expected_output, actual=output,
                                input_value=inputs)
        except:
            self.assertDivisionByZero()

    def test_1_2_3_4_5_6_7_8_9_10_11_12_13_14_15_16_17_18_19_20_0(self):

            """
            The program should print the average of all integers in the sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
            """

            inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "0"]
            output = self.run_exercise(inputs)
            expected_output = "10.5\n"
            self.assertInCustom(expected=expected_output, actual=output,
                                input_value=inputs)


if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner)
