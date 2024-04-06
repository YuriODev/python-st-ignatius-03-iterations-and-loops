import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise48(CustomTestCase):

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

    def test_palindromes_50(self):
        """
        Number of the palindromes between 1 and 50 is 13
        """
        inputs = ["50"]
        output = self.run_exercise(inputs)
        expected_output = "13"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_palindromes_100(self):
        """
        Number of the palindromes between 1 and 100 is 18
        """
        inputs = ["100"]
        output = self.run_exercise(inputs)
        expected_output = "18"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)
    
    def test_palindromes_200(self):
        """
        Number of the palindromes between 1 and 200 is 28
        """
        inputs = ["200"]
        output = self.run_exercise(inputs)
        expected_output = "28"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_palindromes_1000(self):
        """
        Number of the palindromes between 1 and 1000 is 108
        """
        inputs = ["1000"]
        output = self.run_exercise(inputs)
        expected_output = "108"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
