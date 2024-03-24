import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise17(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_number_pattern_1(self):
        """
        The program should print a number pattern according to the input of 6 and 3.
        """

        inputs = ["6", "3"]
        output = self.run_exercise(inputs)
        expected_output = "0\t0\t0\t\n1\t1\t1\t\n2\t2\t2\t\n3\t3\t3\t\n4\t4\t4\t\n5\t5\t5\t\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_number_pattern_2(self):
        """
        The program should print a number pattern according to the input of 3 and 3.
        """

        inputs = ["3", "3"]
        output = self.run_exercise(inputs)
        expected_output = "0\t0\t0\t\n1\t1\t1\t\n2\t2\t2\t\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_number_pattern_3(self):
        """
        The program should print a number pattern according to the input of 3 and 7.
        """

        inputs = ["3", "7"]
        output = self.run_exercise(inputs)
        expected_output = "0\t0\t0\t0\t0\t0\t0\t\n1\t1\t1\t1\t1\t1\t1\t\n2\t2\t2\t2\t2\t2\t2\t\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_number_pattern_4(self):
        """
        The program should print a number pattern according to the input of 4 and 4.
        """

        inputs = ["4", "4"]
        output = self.run_exercise(inputs)
        expected_output = "0\t0\t0\t0\t\n1\t1\t1\t1\t\n2\t2\t2\t2\t\n3\t3\t3\t3\t\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_number_pattern_5(self):
        """
        The program should print a number pattern according to the input of 5 and 5.
        """

        inputs = ["5", "5"]
        output = self.run_exercise(inputs)
        expected_output = "0\t0\t0\t0\t0\t\n1\t1\t1\t1\t1\t\n2\t2\t2\t2\t2\t\n3\t3\t3\t3\t3\t\n4\t4\t4\t4\t4\t\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
