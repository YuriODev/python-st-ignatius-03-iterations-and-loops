import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise31(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_no_list_usage(self):
        """
        The program should not use lists to solve the exercise.
        """

        self.assertNotUsesList()

    def test_example_1(self):
        """
        The program should determine the lowest temperature and whether the temperature has dropped below -18 degrees.
        """

        inputs = ["3", "-20", "2", "-18"]
        output = self.run_exercise(inputs)
        expected_output = "-20\nYes\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_example_2(self):
        """
        The program should determine the lowest temperature and whether the temperature has dropped below -18 degrees.
        """

        inputs = ["5", "-10", "-15", "-20", "-25", "-30"]
        output = self.run_exercise(inputs)
        expected_output = "-30\nYes\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_example_3(self):
        """
        The program should determine the lowest temperature and whether the temperature has dropped below -18 degrees.
        """

        inputs = ["7", "-5", "-10", "-15", "-20", "-25", "-30", "-35"]
        output = self.run_exercise(inputs)
        expected_output = "-35\nYes\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
