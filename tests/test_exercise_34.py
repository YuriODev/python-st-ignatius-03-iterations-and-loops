import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise34(CustomTestCase):

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
        The program should print numbers from 1 to 5.
        """

        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "1\n12\n123\n1234\n12345\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_2(self):
        """
        The program should print numbers from 1 to 3.
        """

        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "1\n12\n123\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_3(self):
        """
        The program should print numbers from 1 to 7.
        """

        inputs = ["7"]
        output = self.run_exercise(inputs)
        expected_output = "1\n12\n123\n1234\n12345\n123456\n1234567\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_4(self):
        """
        The program should print numbers from 1 to 10.
        """

        inputs = ["10"]
        output = self.run_exercise(inputs)
        expected_output = "1\n12\n123\n1234\n12345\n123456\n1234567\n12345678\n123456789\n12345678910\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_5(self):
        """
        The program should print numbers from 1 to 15.
        """

        inputs = ["15"]
        output = self.run_exercise(inputs)
        expected_output = "1\n12\n123\n1234\n12345\n123456\n1234567\n12345678\n123456789\n12345678910\n1234567891011\n123456789101112\n12345678910111213\n1234567891011121314\n123456789101112131415\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
