import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise19(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_sum_of_squares_1(self):
        """
        The program should print a sequence of two-digit numbers, the sum of the squares of the digits of which is divisible by 5.
        """

        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "12, 13, 17, 18, 21, 24, 26, 29, 31, 34, 36, 39, 42, 43, 47, 48, 50, 55, 62, 63, 67, 68, 71, 74, 76, 79, 81, 84, 86, 89, 92, 93, 97, 98, "
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_squares_2(self):
        """
        The program should print a sequence of two-digit numbers, the sum of the squares of the digits of which is divisible by 7.
        """

        inputs = ["7"]
        output = self.run_exercise(inputs)
        expected_output = "70, 77, "
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_squares_3(self):
        """
        The program should print a sequence of two-digit numbers, the sum of the squares of the digits of which is divisible by 10.
        """

        inputs = ["10"]
        output = self.run_exercise(inputs)
        expected_output = "13, 17, 24, 26, 31, 39, 42, 48, 55, 62, 68, 71, 79, 84, 86, 93, 97, "
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_squares_4(self):
        """
        The program should print a sequence of two-digit numbers, the sum of the squares of the digits of which is divisible by 100.
        """

        inputs = ["100"]
        output = self.run_exercise(inputs)
        expected_output = "68, 86, "
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_squares_5(self):
        """
        The program should print a sequence of two-digit numbers, the sum of the squares of the digits of which is divisible by 188.
        """

        inputs = ["162"]
        output = self.run_exercise(inputs)
        expected_output = "99, "
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_squares_6(self):
        """
        The program should print a sequence of two-digit numbers, the sum of the squares of the digits of which is divisible by 1.
        """

        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, "
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner)
