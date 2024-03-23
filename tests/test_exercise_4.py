import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise4(CustomTestCase):

    def test_number_of_hashes_1(self):
        """
        The program should print the number of hashes according to the input.
        """
        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "1 #\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_number_of_hashes_2(self):
        """
        The program should print the number of hashes according to the input.
        """
        inputs = ["2"]
        output = self.run_exercise(inputs)
        expected_output = "1 #\n2 ##\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_number_of_hashes_3(self):
        """
        The program should print the number of hashes according to the input.
        """
        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "1 #\n2 ##\n3 ###\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_number_of_hashes_4(self):
        """
        The program should print the number of hashes according to the input.
        """
        inputs = ["4"]
        output = self.run_exercise(inputs)
        expected_output = "1 #\n2 ##\n3 ###\n4 ####\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_number_of_hashes_5(self):
        """
        The program should print the number of hashes according to the input.
        """
        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "1 #\n2 ##\n3 ###\n4 ####\n5 #####\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_number_of_hashes_6(self):
        """
        The program should print the number of hashes according to the input.
        """
        inputs = ["6"]
        output = self.run_exercise(inputs)
        expected_output = "1 #\n2 ##\n3 ###\n4 ####\n5 #####\n6 ######\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_number_of_hashes_7(self):
        """
        The program should print the number of hashes according to the input.
        """
        inputs = ["7"]
        output = self.run_exercise(inputs)
        expected_output = "1 #\n2 ##\n3 ###\n4 ####\n5 #####\n6 ######\n7 #######\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
