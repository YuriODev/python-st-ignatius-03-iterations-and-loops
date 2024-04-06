import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise35(CustomTestCase):

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

    def test_not_string_conversion(self):
        """
        The program should not convert the input to a string.
        """

        self.assertNotUseStringSlice()

    def test_odd_numbers_descending(self):
        """
        The program should print nothing.
        """

        inputs = ["1"]
        expected_output = "9 7 5 3 1 \n"
        output = self.run_exercise(inputs)
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_odd_numbers_descending_2(self):
        """
        The program should print numbers from 1 to 5.
        """

        inputs = ["2"]
        output = self.run_exercise(inputs)
        expected_output = "99 97 95 93 91 89 87 85 83 81 79 77 75 73 71 69 67 65 63 61 59 57 55 53 51 49 47 45 43 41 39 37 35 33 31 29 27 25 23 21 19 17 15 13 11 \n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
