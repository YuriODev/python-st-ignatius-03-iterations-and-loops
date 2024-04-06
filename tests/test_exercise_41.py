import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise41(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

    def test_no_list_usage(self):
        """
        The program should not use string slicing to solve the exercise.
        """

        self.assertNotUsesList()

    def test_fibonacci_sequence_to_50(self):
        """
        The Fibonacci number 9 is 34
        """
        inputs = ["9"]
        output = self.run_exercise(inputs)
        expected_output = "34"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_fibonacci_sequence_number_2(self):
        """
        The Fibonacci number 10 is 55
        """
        inputs = ["10"]
        output = self.run_exercise(inputs)
        expected_output = "55"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_fibonacci_sequence_number_3(self):
        """
        The Fibonacci number 11 is 89
        """
        inputs = ["11"]
        output = self.run_exercise(inputs)
        expected_output = "89"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_fibonacci_sequence_number_4(self):
        """
        The Fibonacci number 12 is 144
        """
        inputs = ["12"]
        output = self.run_exercise(inputs)
        expected_output = "144"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_fibonacci_sequence_number_5(self):
        """
        The Fibonacci number 13 is 233
        """
        inputs = ["13"]
        output = self.run_exercise(inputs)
        expected_output = "233"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_fibonacci_sequence_number_6(self):
        """
        The Fibonacci number 14 is 377
        """
        inputs = ["14"]
        output = self.run_exercise(inputs)
        expected_output = "377"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
