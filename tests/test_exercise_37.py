import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise37(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_no_math_module_usage(self):
        """
        The program should not use the 'math' module.
        """

        self.assetNotUseMathModule()

    def test_division_without_division(self):
        """
        The program's output for inputs 16 and 5 should be 3 and 1.
        """
        inputs = ["16", "5"]
        output = self.run_exercise(inputs)
        expected_output = "3 1\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)
        
    def test_division_without_division_2(self):
        """
        The program's output for inputs 100 and 25 should be 4 and 0.
        """
        inputs = ["100", "25"]
        output = self.run_exercise(inputs)
        expected_output = "4 0\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_division_without_division_3(self):
        """
        The program's output for inputs 100 and 75 should be 1 and 25.
        """
        inputs = ["100", "75"]
        output = self.run_exercise(inputs)
        expected_output = "1 25\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_division_without_division_4(self):
        """
        The program's output for inputs 100 and 99 should be 1 and 1.
        """
        inputs = ["100", "99"]
        output = self.run_exercise(inputs)
        expected_output = "1 1\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_division_without_division_5(self):
        """
        The program's output for inputs 100 and 100 should be 1 and 0.
        """
        inputs = ["100", "100"]
        output = self.run_exercise(inputs)
        expected_output = "1 0\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
