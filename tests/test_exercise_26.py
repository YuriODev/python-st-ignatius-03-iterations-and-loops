import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise26(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_no_list_usage(self):
        """
        The program should not use a list to solve the exercise.
        """

        self.assertNotUsesList()

    def test_not_string_conversion(self):
        """
        The program should not convert the input to a string.
        """

        self.assertNotUseStringSlice()

    def test_sum_of_digits(self):
        """
        The program should determine the number of three-digit numbers, the sum of the digits of which is equal to a certain integer value `n`, which is entered by the user.
        """

        inputs = ["27"]
        output = self.run_exercise(inputs)
        expected_output = "1\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_digits_2(self):
        """
        The program should determine the number of three-digit numbers, the sum of the digits of which is equal to a certain integer value `n`, which is entered by the user.
        """

        inputs = ["2"]
        output = self.run_exercise(inputs)
        expected_output = "3\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_digits_3(self):
        """
        The program should determine the number of three-digit numbers, the sum of the digits of which is equal to a certain integer value `n`, which is entered by the user.
        """

        inputs = ["20"]
        output = self.run_exercise(inputs)
        expected_output = "36\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_digits_4(self):
        """
        The program should determine the number of three-digit numbers, the sum of the digits of which is equal to a certain integer value `n`, which is entered by the user.
        """

        inputs = ["0"]
        output = self.run_exercise(inputs)
        expected_output = "0\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
