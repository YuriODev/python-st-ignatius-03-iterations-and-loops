
import unittest
import subprocess
import os

class TestExercise27(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_27.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_sum_of_a_series_10(self):
        output = self.run_exercise("10\n")
        self.assertAlmostEqual(float(output.strip()), 3.0418396189294032, places=5)

if __name__ == '__main__':
    unittest.main()
