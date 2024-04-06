import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise2(CustomTestCase):

    def test_m_times_n_10_5(self):
        """
        The program should print the number 10, 5 times.
        """

        inputs = ["10", "5"]
        output = self.run_exercise(inputs)
        expected_output = "10 10 10 10 10"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_m_times_n_10_10(self):
        """
        The program should print the number 10, 10 times.
        """
        inputs = ["10", "10"]
        output = self.run_exercise(inputs)
        expected_output = "10 10 10 10 10 10 10 10 10 10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_m_times_n_5_3(self):
        """
        The program should print the number 5, 3 times.
        """
        inputs = ["5", "3"]
        output = self.run_exercise(inputs)
        expected_output = "5 5 5"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_m_times_n_7_7(self):
        """
        The program should print the number 7, 7 times.
        """
        inputs = ["7", "7"]
        output = self.run_exercise(inputs)
        expected_output = "7 7 7 7 7 7 7"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_m_times_n_1_1(self):
        """
        The program should print the number 1, 1 time.
        """
        inputs = ["1", "1"]
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_m_times_n_0_0(self):
        """
        The program should print nothing.
        """
        inputs = ["0", "0"]
        output = self.run_exercise(inputs)
        expected_output = "\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_m_times_n_3_3(self):
        """
        The program should print the number 3, 3 times.
        """
        inputs = ["3", "3"]
        output = self.run_exercise(inputs)
        expected_output = "3 3 3"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_m_times_n_7_1(self):
        """
        The program should print the number 7, 1 time.
        """
        inputs = ["7", "1"]
        output = self.run_exercise(inputs)
        expected_output = "7"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
