import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise13(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_password_12345(self):
        """
        The program should prompt the user for a password and validate it.
        """

        inputs = ["12345", "111", "45", "12345"]
        output = self.run_exercise(inputs)
        expected_output = "Done\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_password_123(self):
        """
        The program should prompt the user for a password and validate it.
        """

        inputs = ["123", "111", "45", "12345", "123"]
        output = self.run_exercise(inputs)
        expected_output = "Done\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_password_111(self):
        """
        The program should prompt the user for a password and validate it.
        """

        inputs = ["111", "111"]
        output = self.run_exercise(inputs)
        expected_output = "Done\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
