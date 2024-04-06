import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise9(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_multiples_of_2_between_1_and_10(self):
        """
        The program should print multiples of 2 between 1 and 10.
        """
        inputs = ["1", "10", "2"]
        output = self.run_exercise(inputs)
        expected_output = "2 4 6 8 10"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_multiples_of_3_between_1_and_10(self):
        """
        The program should print multiples of 3 between 1 and 10.
        """
        inputs = ["1", "10", "3"]
        output = self.run_exercise(inputs)
        expected_output = "3 6 9"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_multiples_of_4_between_1_and_10(self):
        """
        The program should print multiples of 4 between 1 and 10.
        """
        inputs = ["1", "10", "4"]
        output = self.run_exercise(inputs)
        expected_output = "4 8"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_multiples_of_5_between_1_and_10(self):
        """
        The program should print multiples of 5 between 1 and 10.
        """
        inputs = ["1", "10", "5"]
        output = self.run_exercise(inputs)
        expected_output = "5 10"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_multiples_of_6_between_1_and_10(self):
        """
        The program should print multiples of 6 between 1 and 10.
        """
        inputs = ["1", "10", "6"]
        output = self.run_exercise(inputs)
        expected_output = "6"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_multiples_of_3_between_10_and_20(self):
        """
        The program should print multiples of 3 between 10 and 20.
        """
        inputs = ["10", "20", "3"]
        output = self.run_exercise(inputs)
        expected_output = "12 15 18"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_multiples_of_4_between_10_and_20(self):
        """
        The program should print multiples of 4 between 10 and 20.
        """
        inputs = ["10", "20", "4"]
        output = self.run_exercise(inputs)
        expected_output = "12 16 20"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
