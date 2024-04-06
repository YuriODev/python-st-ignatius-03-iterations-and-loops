import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise47(CustomTestCase):

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

    def test_palindromes_50(self):
        """
        Find the palindromes between 1 and 50
        """
        inputs = ["50"]
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6 7 8 9 11 22 33 44"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_palindromes_100(self):
        """
        Find the palindromes between 1 and 100
        """
        inputs = ["100"]
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)
    
    def test_palindromes_200(self):
        """
        Find the palindromes between 1 and 200
        """
        inputs = ["200"]
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_palindromes_1000(self):
        """
        Find the palindromes between 1 and 1000
        """
        inputs = ["1000"]
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212 222 232 242 252 262 272 282 292 303 313 323 333 343 353 363 373 383 393 404 414 424 434 444 454 464 474 484 494 505 515 525 535 545 555 565 575 585 595 606 616 626 636 646 656 666 676 686 696 707 717 727 737 747 757 767 777 787 797 808 818 828 838 848 858 868 878 888 898 909 919 929 939 949 959 969 979 989 999"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
