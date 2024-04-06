import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise38(CustomTestCase):

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

    def test_even_difference_true(self):
        """
        The program should determine if the difference between the sum of the
        even digits and the sum of the odd digits of a number is equal to 0.
        """

        inputs = ["2134389"]
        output = self.run_exercise(inputs)
        expected_output = "True\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_difference_true_4(self):
        """
        The program should determine if the difference between the sum of the
        even digits and the sum of the odd digits of a number is equal to 0.
        """

        inputs = ["123456789"]
        output = self.run_exercise(inputs)
        expected_output = "True\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_difference_true_2(self):
        """
        The program should determine if the difference between the sum of the
        even digits and the sum of the odd digits of a number is equal to 0.
        """

        inputs = ["2468"]
        output = self.run_exercise(inputs)
        expected_output = "True\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_difference_false_5(self):
        """
        The program should determine if the difference between the sum of the
        even digits and the sum of the odd digits of a number is equal to 0.
        """

        inputs = ["13579"]
        output = self.run_exercise(inputs)
        expected_output = "True\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_difference_true_3(self):
        """
        The program should determine if the difference between the sum of the
        even digits and the sum of the odd digits of a number is equal to 0.
        """

        inputs = ["246137"]
        output = self.run_exercise(inputs)
        expected_output = "True\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_difference_true_6(self):
        """
        The program should determine if the difference between the sum of the
        even digits and the sum of the odd digits of a number is equal to 0.
        """

        inputs = ["1352467"]
        output = self.run_exercise(inputs)
        expected_output = "True\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_difference_false(self):
        """
        The program should determine if the difference between the sum of the
        even digits and the sum of the odd digits of a number is equal to 0.
        """

        inputs = ["1234"]
        output = self.run_exercise(inputs)
        expected_output = "False\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_difference_false_2(self):
        """
        The program should determine if the difference between the sum of the
        even digits and the sum of the odd digits of a number is equal to 0.
        """

        inputs = ["1358"]
        output = self.run_exercise(inputs)
        expected_output = "False\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_difference_false_3(self):
        """
        The program should determine if the difference between the sum of the
        even digits and the sum of the odd digits of a number is equal to 0.
        """

        inputs = ["241"]
        output = self.run_exercise(inputs)
        expected_output = "False\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_difference_false_4(self):
        """
        The program should determine if the difference between the sum of the
        even digits and the sum of the odd digits of a number is equal to 0.
        """

        inputs = ["10"]
        output = self.run_exercise(inputs)
        expected_output = "False\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_difference_false_6(self):
        """
        The program should determine if the difference between the sum of the
        even digits and the sum of the odd digits of a number is equal to 0.
        """

        inputs = ["0"]
        output = self.run_exercise(inputs)
        expected_output = "False\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
