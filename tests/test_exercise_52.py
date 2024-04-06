import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise52(CustomTestCase):

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

    def test_if_statement_usage(self):
        """
        The program should not use the branching construct to solve the exercise.
        """

        self.assertNotUsesIf()

    def test_range_usage(self):
        """
        The program should not use the range function to solve the exercise.
        """

        self.assertNotUseRangeFunction()

    def test_odd_numbers_10_1(self):
        """
        Odd numbers between 10 and 1: 9 7 5 3 1
        """
        inputs = ["10", "1"]
        output = self.run_exercise(inputs)
        expected_output = "9 7 5 3 1"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_odd_numbers_20_1(self):
        """
        Odd numbers between 20 and 1: 19 17 15 13 11 9 7 5 3 1
        """
        inputs = ["20", "1"]
        output = self.run_exercise(inputs)
        expected_output = "19 17 15 13 11 9 7 5 3 1"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_odd_numbers_9_1(self):
        """
        Odd numbers between 9 and 1: 9 7 5 3 1
        """
        inputs = ["9", "1"]
        output = self.run_exercise(inputs)
        expected_output = "9 7 5 3 1"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_odd_numbers_10_2(self):
        """
        Odd numbers between 10 and 2: 9 7 5 3
        """
        inputs = ["10", "2"]
        output = self.run_exercise(inputs)
        expected_output = "9 7 5 3"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
