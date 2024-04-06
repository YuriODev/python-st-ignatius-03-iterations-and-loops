import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise3(CustomTestCase):

    def test_sequence_to_25(self):
        """
        The program should print the numbers from 20 to 25.
        """
        inputs = ["25"]
        output = self.run_exercise(inputs)
        expected_output = "20 21 22 23 24 25"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sequence_to_30(self):
        """
        The program should print the numbers from 20 to 30.
        """
        inputs = ["30"]
        output = self.run_exercise(inputs)
        expected_output = "20 21 22 23 24 25 26 27 28 29 30"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sequence_to_20(self):
        """
        The program should print the number 20.
        """
        inputs = ["20"]
        output = self.run_exercise(inputs)
        expected_output = "20"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
