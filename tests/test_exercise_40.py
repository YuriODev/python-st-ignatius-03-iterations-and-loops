import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise40(CustomTestCase):

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
        The Fibonacci numbers less than 50 are: 1 1 2 3 5 8 13 21 34
        """
        inputs = ["50"]
        output = self.run_exercise(inputs)
        expected_output = "1 1 2 3 5 8 13 21 34"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_fibonacci_sequence_to_100(self):
        """
        The Fibonacci numbers less than 100 are: 1 1 2 3 5 8 13 21 34 55 89
        """
        inputs = ["100"]
        output = self.run_exercise(inputs)
        expected_output = "1 1 2 3 5 8 13 21 34 55 89"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_fibonacci_sequence_to_200(self):
        """
        The Fibonacci numbers less than 200 are: 1 1 2 3 5 8 13 21 34 55 89 144
        """
        inputs = ["200"]
        output = self.run_exercise(inputs)
        expected_output = "1 1 2 3 5 8 13 21 34 55 89 144"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_fibonacci_sequence_to_5(self):
        """
        The Fibonacci numbers less than 5 are: 1 1 2 3
        """

        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_sequence = "1 1 2 3"
        self.assertIn(expected_sequence, output)

    def test_fibonacci_sequence_to_10(self):
        """
        The Fibonacci numbers less than 10 are: 1 1 2 3 5 8
        """
        inputs = ["10"]
        output = self.run_exercise(inputs)
        expected_sequence = "1 1 2 3 5 8"
        self.assertIn(expected_sequence, output)


if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner)
