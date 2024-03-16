
import unittest
import subprocess
import os

class TestExercise13(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_13.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_password_validation_correct(self):
        output = self.run_exercise("12345\n111\n45\n12345\n")
        self.assertIn("Done", output)

    def test_password_validation_incorrect(self):
        output = self.run_exercise("123\n111\n45\n12345\n")
        self.assertIn("Error", output)

if __name__ == '__main__':
    unittest.main()
