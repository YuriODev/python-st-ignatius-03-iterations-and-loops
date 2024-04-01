import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise27(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_sum_of_series(self):
        """
        The program should calculate the sum of the first `n` terms of the series `Pi = 4/1 - 4/3 + 4/5 - 4/7 + ...`.
        """

        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "3.3396825396825403\n"

        self.assertAlmostEqualCustom(expected=expected_output,
                                        input_value=inputs,
                                        actual=output, places=3)

    def test_sum_of_series_2(self):
        """
        The program should calculate the sum of the first `n` terms of the series `Pi = 4/1 - 4/3 + 4/5 - 4/7 + ...`.
        """

        inputs = ["10"]
        output = self.run_exercise(inputs)
        expected_output = "3.3396825396825403\n"
        self.assertAlmostEqualCustom(expected=expected_output,
                                        input_value=inputs,
                                        actual=output, places=3)

    def test_sum_of_series_3(self):
        """
        The program should calculate the sum of the first `n` terms of the series `Pi = 4/1 - 4/3 + 4/5 - 4/7 + ...`.
        """

        inputs = ["15"]
        output = self.run_exercise(inputs)
        expected_output = "3.017071817071818\n"
        self.assertAlmostEqualCustom(expected=expected_output,
                                        input_value=inputs,
                                        actual=output, places=3)

    def test_sum_of_series_4(self):
        """
        The program should calculate the sum of the first `n` terms of the series `Pi = 4/1 - 4/3 + 4/5 - 4/7 + ...`.
        """

        inputs = ["120"]
        output = self.run_exercise(inputs)
        expected_output = "3.1332594798865546\n"
        self.assertAlmostEqualCustom(expected=expected_output,
                                        input_value=inputs,
                                        actual=output, places=3)

    def test_sum_of_series_5(self):
        """
        The program should calculate the sum of the first `n` terms of the series `Pi = 4/1 - 4/3 + 4/5 - 4/7 + ...`.
        """

        inputs = ["500"]
        output = self.run_exercise(inputs)
        expected_output = "3.139592655589783\n"
        self.assertAlmostEqualCustom(expected=expected_output,
                                        input_value=inputs,
                                        actual=output, places=3)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
