import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise42(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

    def test_no_list_usage(self):
        """
        The program should not use string slicing to solve the exercise.
        """

        self.assertNotUsesList()

    def test_greater_than_next_element(self):
        """
        The greatest number that is greater than the next element is 2
        """
        inputs = ["2", "1", "3", "4", "2", "0"]
        output = self.run_exercise(inputs)
        expected_output = "3"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_greater_than_next_element_2(self):
        """
        The greatest number that is greater than the next element is 4
        """
        inputs = ["1", "2", "3", "4", "5", "4", "3", "2", "0"]
        output = self.run_exercise(inputs)
        expected_output = "4"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_greater_than_next_element_3(self):
        """
        The greatest number that is greater than the next element is 3
        """
        inputs = ["1", "2", "3", "4", "3", "2", "1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "4"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_greater_than_next_element_4(self):
        """
        The greatest number that is greater than the next element is 5
        """
        inputs = ["1", "2", "3", "4", "5", "6", "5", "4", "3", "2", "1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "6"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_greater_than_next_element_5(self):
        """
        The greatest number that is greater than the next element is 3
        """
        inputs = ["1", "2", "3", "4", "3", "2", "1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "4"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_greater_than_next_element_0(self):
        """
        The greatest number that is greater than the next element is 1
        """
        inputs = ["1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_greater_than_next_element_1(self):
        """
        The greatest number that is greater than the next element is 2
        """
        inputs = ["1", "2", "0"]
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_greater_than_next_element_none(self):
        """
        There are no numbers greater than the next element
        """
        inputs = ["1", "1", "1", "1", "0"]
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
