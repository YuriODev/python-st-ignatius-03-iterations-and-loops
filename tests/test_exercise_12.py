import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise12(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_divisible_by_125(self):
        """
        The program should calculate the sum of all three-digit numbers that are divisible by 125.
        """

        inputs = ["125"]
        output = self.run_exercise(inputs)
        expected_output = "3500\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_divisible_by_440(self):
        """
        The program should calculate the sum of all three-digit numbers that are divisible by 440.
        """

        inputs = ["440"]
        output = self.run_exercise(inputs)
        expected_output = "1320\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_divisible_by_600(self):
        """
        The program should calculate the sum of all three-digit numbers that are divisible by 600.
        """

        inputs = ["600"]
        output = self.run_exercise(inputs)
        expected_output = "600\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_divisible_by_1000(self):
        """
        The program should calculate the sum of all three-digit numbers that are divisible by 1000.
        """

        inputs = ["1000"]
        output = self.run_exercise(inputs)
        expected_output = "0\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_divisible_by_1(self):
        """
        The program should calculate the sum of all three-digit numbers that are divisible by 1.
        """

        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "494550\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_divisible_by_2(self):
        """
        The program should calculate the sum of all three-digit numbers that are divisible by 2.
        """

        inputs = ["2"]
        output = self.run_exercise(inputs)
        expected_output = "247050\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
