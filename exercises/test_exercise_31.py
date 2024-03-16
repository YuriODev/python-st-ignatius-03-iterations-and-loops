
import unittest
import subprocess
import os

class TestExercise31(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_31.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_lowest_temperature_below_minus_15(self):
        output = self.run_exercise("3\n-20\n2\n-18\n")
        self.assertIn("-20\nYes", output)

if __name__ == '__main__':
    unittest.main()
