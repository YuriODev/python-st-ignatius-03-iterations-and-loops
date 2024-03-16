
import unittest
import subprocess
import os

class TestExercise29(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_29.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_sum_of_squares_until_zero(self):
        output = self.run_exercise("1\n2\n3\n4\n-4\n-3\n-2\n-1\n")
        self.assertEqual(int(output.strip()), 30)

if __name__ == '__main__':
    unittest.main()
