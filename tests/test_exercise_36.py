import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise36(CustomTestCase):

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

    def test_gcd(self):
        """
        The program's output for inputs 8 and 2 should be 2.
        """
        inputs = ["8", "2"]
        output = self.run_exercise(inputs)
        expected_output = "2\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_gcd_2(self):
        """
        The program's output for inputs 12 and 8 should be 4.
        """
        inputs = ["12", "8"]
        output = self.run_exercise(inputs)
        expected_output = "4\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_gcd_3(self):
        """
        The program's output for inputs 100 and 25 should be 25.
        """
        inputs = ["100", "25"]
        output = self.run_exercise(inputs)
        expected_output = "25\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_gcd_4(self):
        """
        The program's output for inputs 100 and 75 should be 25.
        """
        inputs = ["100", "75"]
        output = self.run_exercise(inputs)
        expected_output = "25\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_gcd_5(self):
        """
        The program's output for inputs 100 and 50 should be 50.
        """
        inputs = ["100", "50"]
        output = self.run_exercise(inputs)
        expected_output = "50\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_gcd_6(self):
        """
        The program's output for inputs 10 and 10 should be 10.
        """
        inputs = ["10", "10"]
        output = self.run_exercise(inputs)
        expected_output = "10\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_gcd_7(self):
        """
        The program's output for inputs 0 and 0 should be 0.
        """
        inputs = ["0", "0"]
        try:
            output = self.run_exercise(inputs)
            expected_output = "0.0\n"
            self.assertInCustom(expected=expected_output, actual=output,
                                input_value=inputs)
        except:
            self.assertModuloByZero()


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
