
import unittest
import subprocess
import os

class TestExercise35(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_35.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_odd_numbers_descending(self):
        output = self.run_exercise("1\n")
        expected_output = "9 7 5 3 1\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
