import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise46(CustomTestCase):

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

    def test_position_of_digit(self):
        """
        The position of the digit 3 in the number 1233572 is 4
        """
        inputs = ["1233572", "3"]
        output = self.run_exercise(inputs)
        expected_output = "4"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_position_of_digit_2(self):
        """
        The position of the digit 5 in the number 123456789 is 5
        """
        inputs = ["123456789", "5"]
        output = self.run_exercise(inputs)
        expected_output = "5"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)
    
    def test_position_of_digit_3(self):
        """
        The position of the digit 7 in the number 1233572 is 7
        """
        inputs = ["1233572", "7"]
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)
    
    def test_position_of_digit_4(self):
        """
        The position of the digit 0 in the number 123456789 is 0
        """
        inputs = ["123456789", "0"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)
    
    def test_position_of_digit_5(self):
        """
        The position of the digit 9 in the number 123456789 is 9
        """
        inputs = ["123456789", "9"]
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_position_of_digit_6(self):
        """
        The position of the digit 1 in the number 123456789 is 1
        """
        inputs = ["123456789", "1"]
        output = self.run_exercise(inputs)
        expected_output = "9"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_position_of_digit_7(self):
        """
        The position of the digit 2 in the number 123456789 is 2
        """
        inputs = ["123456789", "2"]
        output = self.run_exercise(inputs)
        expected_output = "8"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
