import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise10(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_pound_to_kg_table_3(self):
        """
        The program should print a table converting pounds to kilograms up to 3 pounds.
        """
        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "1 0.45\n2 0.91\n3 1.36\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_pound_to_kg_table_4(self):
        """
        The program should print a table converting pounds to kilograms up to 4 pounds.
        """
        inputs = ["4"]
        output = self.run_exercise(inputs)
        expected_output = "1 0.45\n2 0.91\n3 1.36\n4 1.81\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_pound_to_kg_table_5(self):
        """
        The program should print a table converting pounds to kilograms up to 5 pounds.
        """
        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "1 0.45\n2 0.91\n3 1.36\n4 1.81\n5 2.27\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_pound_to_kg_table_6(self):
        """
        The program should print a table converting pounds to kilograms up to 6 pounds.
        """
        inputs = ["6"]
        output = self.run_exercise(inputs)
        expected_output = "1 0.45\n2 0.91\n3 1.36\n4 1.81\n5 2.27\n6 2.72\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_pound_to_kg_table_7(self):
        """
        The program should print a table converting pounds to kilograms up to 7 pounds.
        """
        inputs = ["7"]
        output = self.run_exercise(inputs)
        expected_output = "1 0.45\n2 0.91\n3 1.36\n4 1.81\n5 2.27\n6 2.72\n7 3.17\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
