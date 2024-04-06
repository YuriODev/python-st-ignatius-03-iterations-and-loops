import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise53(CustomTestCase):

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

    def test_even_numbers_1_20(self):
        """
        Even numbers between 1 and 20: 2 4 6 8 10 12 14 16 18 20
        """
        inputs = ["1", "20"]
        output = self.run_exercise(inputs)
        expected_output = "2 4 6 8 10 12 14 16 18 20"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_numbers_1_30(self):
        """
        Even numbers between 1 and 30: 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
        """
        inputs = ["1", "30"]
        output = self.run_exercise(inputs)
        expected_output = "2 4 6 8 10 12 14 16 18 20 22 24 26 28 30"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_numbers_1_4(self):
        """
        Even numbers between 1 and 4: 2 4
        """
        inputs = ["1", "4"]
        output = self.run_exercise(inputs)
        expected_output = "2 4"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_numbers_3_7(self):
        """
        Even numbers between 3 and 7: 4 6
        """
        inputs = ["3", "7"]
        output = self.run_exercise(inputs)
        expected_output = "4 6"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
