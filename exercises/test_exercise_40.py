
import unittest
import subprocess
import os

class TestExercise40(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_40.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_fibonacci_sequence_to_50(self):
        output = self.run_exercise("50\n")
        expected_sequence = "1 1 2 3 5 8 13 21 34"
        self.assertIn(expected_sequence, output)

if __name__ == '__main__':
    unittest.main()
