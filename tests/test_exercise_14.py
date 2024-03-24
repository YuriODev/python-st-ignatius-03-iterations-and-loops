import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise14(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_count_of_zeros_1(self):
        """
        The program should count the number of zeros in the input of 4.
        """

        inputs = ["4", "0", "23", "11", "0"]
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_count_of_zeros_2(self):
        """
        The program should count the number of zeros in the input of 3.
        """

        inputs = ["3", "0", "0", "0"]
        output = self.run_exercise(inputs)
        expected_output = "3"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_count_of_zeros_3(self):
        """
        The program should count the number of zeros in the input of 5.
        """

        inputs = ["5", "1", "2", "3", "4", "5"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_count_of_zeros_4(self):
        """
        The program should count the number of zeros in the input of 6.
        """

        inputs = ["6", "0", "0", "0", "0", "0", "0"]
        output = self.run_exercise(inputs)
        expected_output = "6"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_count_of_zeros_5(self):
        """
        The program should count the number of zeros in the input of 7.
        """

        inputs = ["7", "1", "2", "3", "4", "5", "6", "7"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
