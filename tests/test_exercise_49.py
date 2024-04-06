import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise49(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

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

    def test_palindromes_1400_2200(self):
        """
        Palindromes between 1400 and 2200
        """
        inputs = ["1400", "2200"]
        output = self.run_exercise(inputs)
        expected_output = "1441 1551 1661 1771 1881 1991 2002 2112"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_palindromes_1000_2000(self):
        """
        Palindromes between 1000 and 2000
        """
        inputs = ["1000", "2000"]
        output = self.run_exercise(inputs)
        expected_output = "1001 1111 1221 1331 1441 1551 1661 1771 1881 1991"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_palindromes_2000_3000(self):
        """
        Palindromes between 2000 and 3000
        """
        inputs = ["2000", "3000"]
        output = self.run_exercise(inputs)
        expected_output = "2002 2112 2222 2332 2442 2552 2662 2772 2882 2992"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_palindromes_4000_5000(self):
        """
        Palindromes between 4000 and 5000
        """
        inputs = ["4000", "5000"]
        output = self.run_exercise(inputs)
        expected_output = "4004 4114 4224 4334 4444 4554 4664 4774 4884 4994"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
