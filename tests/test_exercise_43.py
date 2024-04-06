import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise43(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

    def test_no_list_usage(self):
        """
        The program should not use string slicing to solve the exercise.
        """

        self.assertNotUsesList()

    def test_second_largest_element(self):
        """
        The second greatest element of the sequence 1, 4, 3, 2, 0 is 3
        """
        inputs = ["1", "4", "3", "2", "0"]
        output = self.run_exercise(inputs)
        expected_output = "3"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_second_largest_element_2(self):
        """
        The second greatest element of the sequence 1, 2, 3, 4, 5, 4, 3, 2, 0 is 4
        """
        inputs = ["1", "2", "3", "4", "5", "4", "3", "2", "0"]
        output = self.run_exercise(inputs)
        expected_output = "4"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)
        
    def test_second_largest_element_3(self):
        """
        The second greatest element of the sequence 1, 2, 3, 4, 3, 2, 1, 0 is 3
        """
        inputs = ["1", "2", "3", "4", "3", "2", "1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "3"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)
    
    def test_second_largest_element_4(self):
        """
        The second greatest element of the sequence 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0 is 5
        """
        inputs = ["1", "2", "3", "4", "5", "6", "5", "4", "3", "2", "1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "5"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_second_largest_element_5(self):
        """
        The second greatest element of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 is 9
        """
        inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "9"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_second_largest_element_6(self):
        """
        The second greatest element of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 is 9
        """
        inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "9"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_second_largest_element_7(self):
        """
        The second greatest element of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 is 9
        """
        inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "9"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_second_largest_element_0(self):
        """
        The second greatest element of the sequence 0, 0 is 0
        """
        inputs = ["0", "0"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
