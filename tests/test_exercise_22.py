import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise22(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_no_string_slicing(self):
        """
        The program should not use string slicing to solve the exercise.
        """

        self.assertNotUseStringSlice()

    def test_138945(self):
        """
        The program should print all integers formed by 138945.
        """

        inputs = ["138945"]
        output = self.run_exercise(inputs)
        expected_output = "13894\n1389\n138\n13\n1\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_123456(self):
        """
        The program should print all integers formed by 123456.
        """

        inputs = ["123456"]
        output = self.run_exercise(inputs)
        expected_output = "12345\n1234\n123\n12\n1\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_987654(self):
        """
        The program should print all integers formed by 987654.
        """

        inputs = ["987654"]
        output = self.run_exercise(inputs)
        expected_output = "98765\n9876\n987\n98\n9\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_1(self):
        """
        The program should print all integers formed by 1.
        """

        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "1\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_0(self):
        """
        The program should print all integers formed by 0.
        """

        inputs = ["0"]
        output = self.run_exercise(inputs)
        expected_output = "0\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_123456789(self):
        """
        The program should print all integers formed by 123456789.
        """

        inputs = ["123456789"]
        output = self.run_exercise(inputs)
        expected_output = "12345678\n1234567\n123456\n12345\n1234\n123\n12\n1\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_987654321(self):
        """
        The program should print all integers formed by 987654321.
        """

        inputs = ["987654321"]
        output = self.run_exercise(inputs)
        expected_output = "98765432\n9876543\n987654\n98765\n9876\n987\n98\n9\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner)
