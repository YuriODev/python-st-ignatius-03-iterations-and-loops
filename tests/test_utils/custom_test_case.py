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

    def check_for_loops(self):
        """
        Checks if the solution file uses 'for' or 'while' loops.
        """
        exercise_file_path = self.get_exercise_path(self.exercise_file_name)
        with open(exercise_file_path, 'r') as file:
            content = file.read()
        return bool(re.search(r'\b(for|while)\b', content))

    def check_for_continue(self):
        """
        Checks if the solution file uses the 'continue' statement.
        """
        exercise_file_path = self.get_exercise_path(self.exercise_file_name)
        with open(exercise_file_path, 'r') as file:
            content = file.read()
        return bool(re.search(r'\bcontinue\b', content))
