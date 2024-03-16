
import unittest
import subprocess
import os

class TestExercise11(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_11.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_sum_of_series_5(self):
        output = self.run_exercise("5\n")
        self.assertAlmostEqual(float(output.strip()), 3.55, places=2)

    def test_sum_of_series_10(self):
        output = self.run_exercise("10\n")
        self.assertAlmostEqual(float(output.strip()), 7.98, places=2)

    def test_sum_of_series_3(self):
        output = self.run_exercise("3\n")
        self.assertAlmostEqual(float(output.strip()), 1.92, places=2)

if __name__ == '__main__':
    unittest.main()
