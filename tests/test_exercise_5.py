import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise5(CustomTestCase):

    def test_loop_usage(self):
        self.assertUsesLoops()

    def test_sum_of_integers_100(self):
        """
        The program should print the sum of all integers from 1 to 100.
        """
        inputs = ["100"]
        output = self.run_exercise(inputs)
        expected_output = "5050\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_sum_of_integers_16(self):
        """
        The program should print the sum of all integers from 1 to 16.
        """
        inputs = ["16"]
        output = self.run_exercise(inputs)
        expected_output = "136\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)
        
    def test_sum_of_integers_1(self):
        """
        The program should print the sum of all integers from 1 to 1.
        """
        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "1\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
