import unittest
import subprocess
import os


class TestExercise13(unittest.TestCase):
    def run_exercise(self, inputs):
        """Helper method to run the exercise script with the provided inputs and return its output."""
        # The inputs list is joined into a single string, each separated by '\n'
        input_value = '\n'.join(inputs) + '\n'
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_13.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_password_12345(self):
        inputs = ["12345", "111", "45", "12345"]
        output = self.run_exercise(inputs)
        self.assertIn("Done", output)

    def test_password_123(self):
        inputs = ["123", "111", "45", "123"]
        output = self.run_exercise(inputs)
        self.assertIn("Done", output)

    def test_password_111(self):
        inputs = ["111", "111"]
        output = self.run_exercise(inputs)
        self.assertIn("Done", output)


if __name__ == '__main__':
    unittest.main()
    print("\x1b[6;30;42m Success! Your code works as intended.\x1b[0m")