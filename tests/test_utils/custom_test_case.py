import unittest
import subprocess
import os
import re
from .test_output_formatter import TestOutputFormatter


class CustomTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        # Set up common properties for all test methods
        self.exercise_file_name = self.determine_exercise_file_name()
        self.exercise_file_path = self.get_exercise_path(self.exercise_file_name)

    @classmethod
    def determine_exercise_file_name(cls):
        """Determines the exercise file name based on the test class name."""
        class_name = cls.__name__
        ex_number = class_name.split("TestExercise")[1]
        return f"exercise_{ex_number}.py"

    @staticmethod
    def get_exercise_path(exercise_file_name):
        """Constructs the absolute path to an exercise file."""
        current_dir = os.path.dirname(__file__)
        project_root = os.path.join(current_dir, "../../exercises")
        return os.path.normpath(os.path.join(project_root, exercise_file_name))

    @property
    def file_content(self):
        """
        Returns the content of the exercise file.
        """
        exercise_file_path = self.exercise_file_path
        with open(exercise_file_path, 'r') as file:
            content = file.read()
        return content

    def run_exercise(self, inputs):
        """Helper method to run the exercise script with the provided inputs and return its output."""
        input_value = '\n'.join(inputs) + '\n'
        return subprocess.check_output(['python3', self.exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def assertInCustom(self, expected, actual, input_value, msg=None):
        try:
            self.assertIn(expected, actual)
        except AssertionError:
            custom_message = TestOutputFormatter.get_failure_details_in_table(input_value, expected.split('\n'), actual.split('\n'))
            if msg:
                custom_message += f"\nAdditional message: {msg}"
            raise AssertionError(custom_message)

    def assertUsesLoops(self):
        """
        Asserts that the solution uses a 'for' or 'while' loop.
        """
        try:
            self.assertTrue(self.check_for_loops())
        except AssertionError:
            loop_usage_message = TestOutputFormatter.generate_loop_usage_message()
            raise AssertionError(loop_usage_message)

    def assertUsesContinue(self):
        """
        Asserts that the solution uses the 'continue' statement.
        """
        try:
            self.assertTrue(self.check_for_continue())
        except AssertionError:
            continue_usage_message = TestOutputFormatter.generate_continue_usage_message()
            raise AssertionError(continue_usage_message)

    def assertNotUsesIf(self):
        """
        Asserts that the solution does not use the 'if' statement.
        """
        try:
            self.assertFalse(self.check_for_if())
        except AssertionError:
            if_usage_message = TestOutputFormatter.generate_if_usage_message()
            raise AssertionError(if_usage_message)

    def assertNotUsesList(self):
        """
        Asserts that the solution does not use lists.
        """
        try:
            self.assertFalse(self.check_for_list())
        except AssertionError:
            list_usage_message = TestOutputFormatter.generate_list_usage_message()
            raise AssertionError(list_usage_message)

    def assertNotUseStringSlice(self):
        """
        Asserts that the solution does not use string slicing.
        """
        try:
            self.assertFalse(self.check_for_string_slice())
        except AssertionError:
            string_slice_message = TestOutputFormatter.generate_string_slice_message()
            raise AssertionError(string_slice_message)

    def assetNotUseMathModule(self):
        """
        Asserts that the solution does not use the 'math' module.
        """
        try:
            self.assertFalse(self.check_for_math_module())
        except AssertionError:
            message = TestOutputFormatter.generate_math_module_usage_message()
            raise AssertionError(message)

    def assertDivisionByZero(self):
        """
        Asserts that the solution does not divide by zero.
        """

        division_by_zero_message = TestOutputFormatter.generate_division_by_zero_message()
        raise AssertionError(division_by_zero_message)

    def assertModuloByZero(self):
        """
        Asserts that the solution does not use the modulo operator with zero.
        """
        try:
            self.assertNotIn("% 0", self.file_content)
        except AssertionError:
            message = TestOutputFormatter.generate_modulo_division_by_zero_message( )
            raise AssertionError(message)

    def assertNoProductSymbolUsage(self):
        """
        Asserts that the solution does not use the '*' symbol to calculate the product.
        """
        try:
            self.assertFalse(self.check_for_product_symbol())
        except AssertionError:
            message = TestOutputFormatter.generate_product_symbol_usage_message()
            raise AssertionError(message)
        
    def assertNoDivisionSymbolUsage(self):
        """
        Asserts that the solution does not use the '/' symbol to calculate the division.
        """
        try:
            self.assertFalse(self.check_for_division_symbol())
        except AssertionError:
            message = TestOutputFormatter.generate_division_operator_usage_message()
            raise AssertionError(message)

    def assertNoIntegerDivision(self):
        """
        Asserts that the solution does not use integer division.
        """
        try:
            self.assertFalse(self.check_for_integer_division())
        except AssertionError:
            message = TestOutputFormatter.generate_integer_division_operator_usage_message()
            raise AssertionError(message)

    def assertNoModulos(self):
        """
        Asserts that the solution does not use the modulo operator.
        """
        try:
            self.assertFalse(self.check_for_modulos())
        except AssertionError:
            message = TestOutputFormatter.generate_modulo_operator_usage_message()
            raise AssertionError(message)

    def assertAlmostEqualCustom(self, expected, actual, input_value, places=None, msg=None):
        """
        Asserts that two floating-point numbers are equal up to a certain number of decimal places.
        """
        try:
            # Remove non digit elements from the output
            actual = ''.join(list(filter(str.isdigit, actual)))
            self.assertAlmostEqual(float(expected), float(actual), places)
        except AssertionError:
            custom_message = TestOutputFormatter.get_failure_details_in_table(input_value, expected.split('\n'), actual.split('\n'))
            if msg:
                custom_message += f"\nAdditional message: {msg}"

    def assertNotUseSumFunction(self):
        """
        Asserts that the solution does not use the 'sum' function.
        """
        try:
            self.assertFalse(self.check_for_sum_function_usage())
        except AssertionError:
            message = TestOutputFormatter.generate_sum_function_usage_message()
            raise AssertionError(message)

    def assertNotUseRangeFunction(self):
        """
        Asserts that the solution does not use the 'range' function.
        """
        try:
            self.assertFalse(self.check_for_range_function_usage())
        except AssertionError:
            message = TestOutputFormatter.generate_range_function_usage_message()
            raise AssertionError(message)
        
    def check_for_range_function_usage(self):
        """
        Checks if the solution file uses the 'range' function.
        """
        content = self.file_content
        return bool(re.search(r'range\(', content))

    def check_for_sum_function_usage(self):
        """
        Checks if the solution file uses the 'sum' function.
        """
        content = self.file_content
        return bool(re.search(r'sum\(', content))

    def check_for_loops(self):
        """
        Checks if the solution file uses 'for' or 'while' loops.
        """
        content = self.file_content
        return bool(re.search(r'\b(for|while)\b', content))

    def check_for_continue(self):
        """
        Checks if the solution file uses the 'continue' statement.
        """
        content = self.file_content
        return bool(re.search(r'\bcontinue\b', content))

    def check_for_if(self):
        """
        Checks if the solution file uses the 'if' statement.
        """
        content = self.file_content
        return bool(re.search(r'\bif\b', content))

    def check_for_list(self):
        """
        Checks if the solution file uses lists or list constructions.
        """
        content = self.file_content
        return bool(re.search(r'\blist\b|\[|\]', content))

    def check_for_string_slice(self):
        """
        Checks if the solution file uses string slicing or str function
        """
        content = self.file_content
        return bool(re.search(r'\[.*:.*\]', content)) or bool(re.search(r'str\(', content))

    def check_for_product_symbol(self):
        """
        Checks if the solution file uses the '*' symbol to calculate the product.
        """
        content = self.file_content
        return bool(re.search(r'\*', content))

    def check_for_division_symbol(self):
        """
        Checks if the solution file uses the '/' symbol to calculate the division.
        """
        content = self.file_content
        return bool(re.search(r'/', content))

    def check_for_integer_division(self):
        """
        Checks if the solution file uses integer division.
        """
        content = self.file_content
        return bool(re.search(r'//', content))

    def check_for_modulos(self):
        """
        Checks if the solution file uses the modulo operator.
        """
        content = self.file_content
        return bool(re.search(r'%', content))

    def check_for_math_module(self):
        """
        Checks if the solution file uses the 'math' module.
        """
        content = self.file_content
        return bool(re.search(r'import math', content)) or bool(re.search(r'import', content))