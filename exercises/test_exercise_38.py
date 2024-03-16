
import unittest
import subprocess
import os

class TestExercise38(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_38.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_even_difference_true(self):
        output = self.run_exercise("2134389\n")
        self.assertIn("True", output)

    def test_even_difference_false(self):
        output = self.run_exercise("1234\n")
        self.assertIn("False", output)

if __name__ == '__main__':
    unittest.main()
