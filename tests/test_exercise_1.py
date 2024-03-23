import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise1(CustomTestCase):

    def test_countdown_5(self):
        """
        The countdown should print the numbers from 5 down to 1 and
        then print 'Start!'
        """

        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "5\n4\n3\n2\n1\nStart!\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_countdown_3(self):
        """
        The countdown should print the numbers from 3 down to 1 and
        then print 'Start!'
        """
        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "3\n2\n1\nStart!\n"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_countdown_7(self):
        """
        The countdown should print the numbers from 7 down to 1 and
        then print 'Start!'
        """
        inputs = ["7"]
        output = self.run_exercise(inputs)
        expected_output = "7\n6\n5\n4\n3\n2\n1\nStart!\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
