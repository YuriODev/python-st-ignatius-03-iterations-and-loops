import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise21(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_factorial_1(self):
        """
        The program should calculate the factorial of 1.
        """

        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_factorial_2(self):
        """
        The program should calculate the factorial of 2.
        """

        inputs = ["2"]
        output = self.run_exercise(inputs)
        expected_output = "3"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_factorial_3(self):
        """
        The program should calculate the factorial of 3.
        """

        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "9"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_factorial_4(self):
        """
        The program should calculate the factorial of 4.
        """

        inputs = ["4"]
        output = self.run_exercise(inputs)
        expected_output = "33"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_factorials_1(self):
        """
        The program should calculate the sum of the factorials of all integers from 1 to 3.
        """

        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "9"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_factorials_2(self):
        """
        The program should calculate the sum of the factorials of all integers from 1 to 4.
        """

        inputs = ["4"]
        output = self.run_exercise(inputs)
        expected_output = "33"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_factorials_3(self):
        """
        The program should calculate the sum of the factorials of all integers from 1 to 5.
        """

        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "153"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_factorials_4(self):
        """
        The program should calculate the sum of the factorials of all integers from 1 to 6.
        """

        inputs = ["6"]
        output = self.run_exercise(inputs)
        expected_output = "873"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_factorials_5(self):
        """
        The program should calculate the sum of the factorials of all integers from 1 to 7.
        """

        inputs = ["7"]
        output = self.run_exercise(inputs)
        expected_output = "5913"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_factorials_6(self):
        """
        The program should calculate the sum of the factorials of all integers from 1 to 8.
        """

        inputs = ["8"]
        output = self.run_exercise(inputs)
        expected_output = "46233"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner)
