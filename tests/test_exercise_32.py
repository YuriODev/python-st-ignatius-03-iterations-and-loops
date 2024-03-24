import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise32(CustomTestCase):

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

    def test_3_15_25_140(self):
        """
        The program should print the difference between the maximum and minimum speeds of the cars and the number of cars whose speed did not exceed 30 km/h.
        """

        inputs = ["3", "15", "25", "140"]
        output = self.run_exercise(inputs)
        expected_output = "125\n2\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_5_10_20_30_40_50(self):
        """
        The program should print the difference between the maximum and minimum speeds of the cars and the number of cars whose speed did not exceed 30 km/h.
        """

        inputs = ["5", "10", "20", "30", "40", "50"]
        output = self.run_exercise(inputs)
        expected_output = "40\n3\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_7_5_10_15_20_25_30_35(self):
        """
        The program should print the difference between the maximum and minimum speeds of the cars and the number of cars whose speed did not exceed 30 km/h.
        """

        inputs = ["7", "5", "10", "15", "20", "25", "30", "35"]
        output = self.run_exercise(inputs)
        expected_output = "30\n6\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_1_1(self):
        """
        The program should print the difference between the maximum and minimum speeds of the cars and the number of cars whose speed did not exceed 30 km/h.
        """

        inputs = ["1", "1"]
        output = self.run_exercise(inputs)
        expected_output = "0\n1\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_1_300(self):
        """
        The program should print the difference between the maximum and minimum speeds of the cars and the number of cars whose speed did not exceed 30 km/h.
        """

        inputs = ["1", "300"]
        output = self.run_exercise(inputs)
        expected_output = "0\n0\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
