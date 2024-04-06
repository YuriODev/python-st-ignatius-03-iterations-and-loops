import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise45(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

    def test_no_list_usage(self):
        """
        The program should not use string slicing to solve the exercise.
        """

        self.assertNotUsesList()

    def test_index_of_largest_element(self):
        """
        The sign changes in the sequence -5, -3, 10, 6, -4, 7, -1, 0 is 4
        """
        inputs = ["-5", "-3", "10", "6", "-4", "7", "-1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "4"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_no_sign_changes(self):
        """
        The sign changes in the sequence 1, 2, 3, 4, 5, 6, 7, 8 is 0
        """
        inputs = ["1", "2", "3", "4", "5", "6", "7", "0"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_no_sign_changes_2(self):
        """
        The sign changes in the sequence 1, 2, 3, 4, 5, 6, 7, 8 is 0
        """
        inputs = ["-1", "-2", "-3", "-4", "-5", "-6", "-7", "0"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sign_changes_2(self):
        """
        The sign changes in the sequence 5, 3, 10, 6, -4, 7, 1, 0 is 3
        """
        inputs = ["5", "3", "10", "6", "-4", "7", "1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sign_changes_3(self):
        """
        The sign changes in the sequence -5, 3, 10, 6, -4, 7, 1, 0 is 3
        """
        inputs = ["-5", "3", "10", "6", "-4", "7", "1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "3"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sign_changes_4(self):
        """
        The sign changes in the sequence -5, -3, -10, -6, -4, -7, -1, 0 is 0
        """
        inputs = ["-5", "-3", "-10", "-6", "-4", "-7", "-1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sign_changes_5(self):
        """
        The sign changes in the sequence 5, 3, 10, 6, 4, 7, 1, 0 is 0
        """
        inputs = ["5", "3", "10", "6", "4", "7", "1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
