
import unittest
import subprocess
import os

class TestExercise33(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_33.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_two_dimensional_table(self):
        output = self.run_exercise("5\n")
        expected_output = "0\t1\t1\t1\t1\n-1\t0\t1\t1\t1\n-1\t-1\t0\t1\t1\n-1\t-1\t-1\t0\t1\n-1\t-1\t-1\t-1\t0\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
