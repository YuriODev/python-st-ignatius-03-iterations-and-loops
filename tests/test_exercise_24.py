import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise24(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_3_6_9_8_0(self):
        """
        The program should print the number of even elements in the sequence.
        """

        inputs = ["3", "6", "9", "8", "0"]
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_1_2_3_4_5_0(self):
        """
        The program should print the number of even elements in the sequence.
        """

        inputs = ["1", "2", "3", "4", "5", "0"]
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_10_20_30_40_50_0(self):
        """
        The program should print the number of even elements in the sequence.
        """

        inputs = ["10", "20", "30", "40", "50", "0"]
        output = self.run_exercise(inputs)
        expected_output = "5"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_0(self):
        """
        The program should print the number of even elements in the sequence.
        """

        inputs = ["0"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_1(self):
        """
        The program should print the number of even elements in the sequence.
        """

        inputs = ["1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
