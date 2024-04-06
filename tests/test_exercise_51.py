import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise51(CustomTestCase):

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

    def test_three_identical_digits_1000_1200(self):
        """
        Numbers with 3 identical digits between 1000 and 1200: 1000 1011 1101 1111 1121 1131 1141 1151 1161 1171 1181 1191
        """
        inputs = ["1000", "1200"]
        output = self.run_exercise(inputs)
        expected_output = "1000 1011 1101 1110 1111 1112 1113 1114 1115 1116 1117 1118 1119 1121 1131 1141 1151 1161 1171 1181 1191"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_three_identical_digits_2169_2190(self):
        """
        Numbers with 3 identical digits between 2169 and 2190: 2177 2188 2199
        """
        inputs = ["2169", "2290"]
        output = self.run_exercise(inputs)
        expected_output = "2220"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_three_identical_digits_3000_3100(self):
        """
        Numbers with 3 identical digits between 3000 and 3100: 3000 3033
        """
        inputs = ["3000", "3100"]
        output = self.run_exercise(inputs)
        expected_output = "3000 3033"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_three_identical_digits_9000_9999(self):
        """
        Numbers with 3 identical digits between 9000 and 9999: 9000 9111 9222 9333 9444 9555 9666 9777 9888 9999
        """
        inputs = ["9000", "9999"]
        output = self.run_exercise(inputs)
        expected_output = "9000 9099 9111 9199 9222 9299 9333 9399 9444 9499 9555 9599 9666 9699 9777 9799 9888 9899 9909 9919 9929 9939 9949 9959 9969 9979 9989 9990 9991 9992 9993 9994 9995 9996 9997 9998"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
