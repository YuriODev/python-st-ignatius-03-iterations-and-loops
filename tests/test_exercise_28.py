import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise28(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_no_asterisk(self):
        """
        The program should not use the multiplication operation to calculate the product of two numbers.
        """

        self.assertNoProductSymbolUsage()

    def test_product_of_two_numbers(self):
        """
        The program should prompt the user to enter two integers, `a` and `b`, and output their product without using the multiplication operation.
        """

        inputs = ["7", "8"]
        output = self.run_exercise(inputs)
        expected_output = "56\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_product_of_two_numbers_2(self):
        """
        The program should prompt the user to enter two integers, `a` and `b`, and output their product without using the multiplication operation.
        """

        inputs = ["5", "6"]
        output = self.run_exercise(inputs)
        expected_output = "30\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_product_of_two_numbers_3(self):
        """
        The program should prompt the user to enter two integers, `a` and `b`, and output their product without using the multiplication operation.
        """

        inputs = ["3", "4"]
        output = self.run_exercise(inputs)
        expected_output = "12\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_product_of_two_numbers_4(self):
        """
        The program should prompt the user to enter two integers, `a` and `b`, and output their product without using the multiplication operation.
        """

        inputs = ["10", "10"]
        output = self.run_exercise(inputs)
        expected_output = "100\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs) 


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
