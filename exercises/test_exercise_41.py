import unittest
import subprocess
import os

class TestExercise41(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_41.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_fibonacci_sequence_number(self):
        output = self.run_exercise("9\\n")
        self.assertEqual(int(output.strip()), 34)

if __name__ == '__main__':
    unittest.main()
