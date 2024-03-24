import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise20(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_if_statement_usage(self):
        """
        The program should not use the branching construct to solve the exercise.
        """

        self.assertNotUsesIf()

    def test_list_usage(self):
        """
        The program should not use lists to solve the exercise.
        """

        self.assertNotUsesList()

    def test_odd_numbers_1(self):
        """
        The program should print all odd numbers from 1 to 15.
        """

        inputs = ["15"]
        output = self.run_exercise(inputs)
        expected_output = "1 3 5 7 9 11 13 15 "
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_odd_numbers_2(self):
        """
        The program should print all odd numbers from 1 to 8.
        """

        inputs = ["8"]
        output = self.run_exercise(inputs)
        expected_output = "1 3 5 7 "
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_odd_numbers_3(self):
        """
        The program should print all odd numbers from 1 to 5.
        """

        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "1 3 5 "
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_odd_numbers_4(self):
        """
        The program should print all odd numbers from 1 to 1.
        """

        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "1 "
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_odd_numbers_5(self):
        """
        The program should print all odd numbers from 1 to 10.
        """

        inputs = ["10"]
        output = self.run_exercise(inputs)
        expected_output = "1 3 5 7 9 "
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_odd_numbers_6(self):
        """
        The program should print all odd numbers from 1 to 20.
        """

        inputs = ["20"]
        output = self.run_exercise(inputs)
        expected_output = "1 3 5 7 9 11 13 15 17 19 "
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner)
