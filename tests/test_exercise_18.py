import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise18(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_total_number_of_errors_1(self):
        """
        The program should determine the total number of errors collected over 6 days.
        """

        inputs = ["6", "45", "101", "67", "43", "21", "0"]
        output = self.run_exercise(inputs)
        expected_output = "277"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_total_number_of_errors_2(self):
        """
        The program should determine the total number of errors collected over 3 days.
        """

        inputs = ["3", "0", "0", "0"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_total_number_of_errors_3(self):
        """
        The program should determine the total number of errors collected over 5 days.
        """

        inputs = ["5", "1", "2", "3", "4", "5"]
        output = self.run_exercise(inputs)
        expected_output = "15"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_total_number_of_errors_4(self):
        """
        The program should determine the total number of errors collected over 7 days.
        """

        inputs = ["7", "1", "2", "3", "4", "5", "6", "7"]
        output = self.run_exercise(inputs)
        expected_output = "28"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_total_number_of_errors_5(self):
        """
        The program should determine the total number of errors collected over 4 days.
        """

        inputs = ["4", "1", "2", "3", "4"]
        output = self.run_exercise(inputs)
        expected_output = "10"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)
        
    def test_total_number_of_errors_6(self):
        """
        The program should determine the total number of errors collected over 2 days.
        """

        inputs = ["2", "1", "1"]
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner)
