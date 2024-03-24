import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise11(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_sum_of_series_5(self):
        """
        The program should calculate the sum of the series up to 5.
        """

        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "3.55\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_series_10(self):
        """
        The program should calculate the sum of the series up to 10.
        """

        inputs = ["10"]
        output = self.run_exercise(inputs)
        expected_output = "7.98\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_series_3(self):
        """
        The program should calculate the sum of the series up to 3.
        """

        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "1.92\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_series_1(self):
        """
        The program should calculate the sum of the series up to 1.
        """

        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "0.50\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_series_2(self):
        """
        The program should calculate the sum of the series up to 2.
        """

        inputs = ["2"]
        output = self.run_exercise(inputs)
        expected_output = "1.17\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
