import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise8(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_continue_usage(self):
        """
        The program should use the 'continue' statement to skip odd numbers.
        """

        self.assertUsesContinue()

    def test_even_numbers_1(self):
        """
        The program should print even numbers up to 1.
        """

        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_numbers_2(self):
        """
        The program should print even numbers up to 2.
        """

        inputs = ["2"]
        output = self.run_exercise(inputs)
        expected_output = "2\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_numbers_3(self):
        """
        The program should print even numbers up to 3.
        """

        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "2\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_numbers_4(self):
        """
        The program should print even numbers up to 4.
        """

        inputs = ["4"]
        output = self.run_exercise(inputs)
        expected_output = "2 4\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_numbers_5(self):
        """
        The program should print even numbers up to 5.
        """

        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "2 4\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_numbers_6(self):
        """
        The program should print even numbers up to 6.
        """

        inputs = ["6"]
        output = self.run_exercise(inputs)
        expected_output = "2 4 6\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_even_numbers_10(self):
        """
        The program should print even numbers up to 10.
        """
        inputs = ["10"]
        output = self.run_exercise(inputs)
        expected_output = "2 4 6 8 10\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
