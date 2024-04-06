import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise39(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

    def test_no_list_usage(self):
        """
        The program should not use string slicing to solve the exercise.
        """

        self.assertNotUsesList()

    def test_not_string_conversion(self):
        """
        The program should not convert the input to a string.
        """

        self.assertNotUseStringSlice()

    def test_no_sum_function_usage(self):
        """
        The program should not use the 'sum' function to solve the exercise.
        """

        self.assertNotUseSumFunction()

    def test_sum_of_digits_positive(self):
        """
        The program should determine if the difference between the sum of the
        even digits and the sum of the odd digits of a number is equal to 0.
        """

        inputs = ["123"]
        output = self.run_exercise(inputs)
        expected_output = "6\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_digits_negative(self):
        """
        Sum of the digits in the number -123 is 6.
        """
        inputs = ["-123"]
        output = self.run_exercise(inputs)
        expected_output = "6\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_digits_zero(self):
        """
        Sum of the digits in the number 0 is 0.
        """
        inputs = ["0"]
        output = self.run_exercise(inputs)
        expected_output = "0\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_digits_single_digit(self):
        """
        Sum of the digits in the number 5 is 5.
        """
        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "5\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_digits_single_digit_negative(self):
        """
        Sum of the digits in the number -5 is 5.
        """
        inputs = ["-5"]
        output = self.run_exercise(inputs)
        expected_output = "5\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_digits_large_number(self):
        """
        Sum of the digits in the number 123456789 is 45.
        """
        inputs = ["123456789"]
        output = self.run_exercise(inputs)
        expected_output = "45\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_digits_large_number_negative(self):
        """
        Sum of the digits in the number -123456789 is 45.
        """
        inputs = ["-123456789"]
        output = self.run_exercise(inputs)
        expected_output = "45\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_digits_large_number_zero(self):
        """
        Sum of the digits in the number 1234567890 is 45.
        """
        inputs = ["1234567890"]
        output = self.run_exercise(inputs)
        expected_output = "45\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
