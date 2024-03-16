
import unittest
import subprocess
import os

class TestExercise37(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_37.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_division_without_division(self):
        output = self.run_exercise("16\n5\n")
        results = output.strip().split()
        self.assertEqual(results, ['3', '1'])

if __name__ == '__main__':
    unittest.main()
