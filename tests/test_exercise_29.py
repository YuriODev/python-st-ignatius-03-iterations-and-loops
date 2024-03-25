import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise29(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_sum_of_squares(self):
        """
        The program should read numbers (one per line) until the sum of the entered numbers equals 0, and immediately after that, output the sum of the squares of all the entered numbers.
        """

        inputs = ["1", "2", "3", "4", "-4", "-3", "-2", "-1"]
        output = self.run_exercise(inputs)
        expected_output = "60\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_squares_2(self):
        """
        The program should read numbers (one per line) until the sum of the entered numbers equals 0, and immediately after that, output the sum of the squares of all the entered numbers.
        """

        inputs = ["1", "2", "3", "4", "-10"]
        output = self.run_exercise(inputs)
        expected_output = "130\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_squares_3(self):
        """
        The program should read numbers (one per line) until the sum of the entered numbers equals 0, and immediately after that, output the sum of the squares of all the entered numbers.
        """

        inputs = ["1", "2", "3", "4", "-1", "-2", "-3", "-4"]
        output = self.run_exercise(inputs)
        expected_output = "60\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_squares_4(self):
        """
        The program should read numbers (one per line) until the sum of the entered numbers equals 0, and immediately after that, output the sum of the squares of all the entered numbers.
        """

        inputs = ["1", "-15", "14"]
        output = self.run_exercise(inputs)
        expected_output = "422\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


    
if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
