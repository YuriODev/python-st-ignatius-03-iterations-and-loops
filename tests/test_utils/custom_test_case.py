import unittest
import subprocess
import os
from .test_output_formatter import TestOutputFormatter


class CustomTestCase(unittest.TestCase):

    @staticmethod
    def get_exercise_path(exercise_file_name):
        """Constructs the absolute path to an exercise file."""
        current_dir = os.path.dirname(__file__)
        project_root = os.path.join(current_dir, "../..")
        return os.path.normpath(os.path.join(project_root, "exercises", exercise_file_name))

    @property
    def exercise_file_name(self):
        class_name = self.__class__.__name__
        ex_number = class_name.split("TestExercise")[1]
        return f"exercise_{ex_number}.py"

    def run_exercise(self, inputs):
            """Helper method to run the exercise script with the provided inputs and return its output."""
            # The inputs list is joined into a single string, each separated by '\n'
            input_value = '\n'.join(inputs) + '\n'
            exercise_file_path = self.get_exercise_path(self.exercise_file_name)
            return subprocess.check_output(['python3', exercise_file_path], input=input_value.encode(), text=True)

    def assertInCustom(self, expected, actual, input_value, msg=None):

        """
        Custom assertIn method to catch assertion errors and customize the error message.
        """
        try:
            self.assertIn(expected, actual)
        except AssertionError:
            custom_message = TestOutputFormatter.get_failure_details_in_table(input_value, expected.split('\n'), actual.split('\n'))
            if msg:
                custom_message += f"\nAdditional message: {msg}"
            raise AssertionError(custom_message)
