import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise7(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_star_pattern_1(self):
        """
        The program should print a hash pattern according to the input of 1.
        """

        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "##\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_star_pattern_2(self):
        """
        The program should print a hash pattern according to the input of 2.
        """

        inputs = ["2"]
        output = self.run_exercise(inputs)
        expected_output = "##\n# #\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_hash_pattern_3(self):
        """
        The program should print a hash pattern according to the input of 3.
        """
        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "##\n# #\n#  #\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_hash_pattern_4(self):
        """
        The program should print a hash pattern according to the input of 4.
        """
        inputs = ["4"]
        output = self.run_exercise(inputs)
        expected_output = "##\n# #\n#  #\n#   #\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_hash_pattern_5(self):
        """
        The program should print a hash pattern according to the input of 5.
        """
        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "##\n# #\n#  #\n#   #\n#    #\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_hash_pattern_6(self):
        """
        The program should print a hash pattern according to the input of 6.
        """
        inputs = ["6"]
        output = self.run_exercise(inputs)
        expected_output = "##\n# #\n#  #\n#   #\n#    #\n#     #\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_hash_pattern_7(self):
        """
        The program should print a hash pattern according to the input of 7.
        """
        inputs = ["7"]
        output = self.run_exercise(inputs)
        expected_output = "##\n# #\n#  #\n#   #\n#    #\n#     #\n#      #\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())