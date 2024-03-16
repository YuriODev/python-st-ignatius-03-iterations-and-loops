
import unittest
import subprocess
import os

class TestExercise36(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_36.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_gcd(self):
        output = self.run_exercise("8\n2\n")
        self.assertEqual(int(output.strip()), 2)

if __name__ == '__main__':
    unittest.main()
