
import unittest
import subprocess
import os

class TestExercise25(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_25.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_car_distance(self):
        output = self.run_exercise("10\n200\n")
        self.assertIn("km, 33 days", output)

if __name__ == '__main__':
    unittest.main()
