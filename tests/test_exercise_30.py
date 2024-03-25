import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise30(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_1_hour(self):
        """
        The program should calculate the number of cells after 1 hour.
        """

        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "1\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_2_hours(self):
        """
        The program should calculate the number of cells after 2 hours.
        """

        inputs = ["2"]
        output = self.run_exercise(inputs)
        expected_output = "1\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_3_hours(self):
        """
        The program should calculate the number of cells after 3 hours.
        """

        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "2\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_6_hours(self):
        """
        The program should calculate the number of cells after 6 hours.
        """

        inputs = ["6"]
        output = self.run_exercise(inputs)
        expected_output = "4\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_9_hours(self):
        """
        The program should calculate the number of cells after 9 hours.
        """

        inputs = ["9"]
        output = self.run_exercise(inputs)
        expected_output = "8\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_12_hours(self):
        """
        The program should calculate the number of cells after 12 hours.
        """

        inputs = ["12"]
        output = self.run_exercise(inputs)
        expected_output = "16\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_15_hours(self):
        """
        The program should calculate the number of cells after 15 hours.
        """

        inputs = ["15"]
        output = self.run_exercise(inputs)
        expected_output = "32\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_18_hours(self):
        """
        The program should calculate the number of cells after 18 hours.
        """

        inputs = ["18"]
        output = self.run_exercise(inputs)
        expected_output = "64\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)
        
    def test_21_hours(self):
        """
        The program should calculate the number of cells after 21 hours.
        """

        inputs = ["21"]
        output = self.run_exercise(inputs)
        expected_output = "128\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_24_hours(self):
        """
        The program should calculate the number of cells after 24 hours.
        """

        inputs = ["24"]
        output = self.run_exercise(inputs)
        expected_output = "256\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
