
import unittest
import subprocess
import os

class TestExercise15(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_15.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_error_collection(self):
        output = self.run_exercise("6\n45\n101\n67\n43\n21\n0\n")
        self.assertEqual(int(output.strip()), 277)

    def test_all_zeros(self):
        output = self.run_exercise("3\n0\n0\n0\n")
        self.assertEqual(int(output.strip()), 0)

    def test_varied_errors(self):
        output = self.run_exercise("5\n1\n2\n3\n4\n5\n")
        self.assertEqual(int(output.strip()), 15)

if __name__ == '__main__':
    unittest.main()
