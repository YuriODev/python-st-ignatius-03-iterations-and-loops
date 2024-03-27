import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise33(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_no_list_usage(self):
        """
        The program should not use string slicing to solve the exercise.
        """

        self.assertNotUsesList()

    def test_0(self):
        """
        The program should print nothing.
        """

        inputs = ["0"]
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_1(self):
        """
        The program should print a 0.
        """

        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_2(self):
        """
        The program should print a two-dimensional table with the values of the exercise.
        """

        inputs = ["2"]
        output = self.run_exercise(inputs)
        expected_output = "0\t1\t\n-1\t0\t\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_3(self):
        """
        The program should print a two-dimensional table with the values of the exercise.
        """

        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "0\t1\t1\t\n-1\t0\t1\t\n-1\t-1\t0\t\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_4(self):
        """
        The program should print a two-dimensional table with the values of the exercise.
        """

        inputs = ["4"]
        output = self.run_exercise(inputs)
        expected_output = "0\t1\t1\t1\t\n-1\t0\t1\t1\t\n-1\t-1\t0\t1\t\n-1\t-1\t-1\t0\t\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_5(self):
        """
        The program should print a two-dimensional table with the values of the exercise.
        """

        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "0\t1\t1\t1\t1\t\n-1\t0\t1\t1\t1\t\n-1\t-1\t0\t1\t1\t\n-1\t-1\t-1\t0\t1\t\n-1\t-1\t-1\t-1\t0\t\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
