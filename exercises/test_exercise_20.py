
import unittest
import subprocess
import os

class TestExercise20(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_20.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_odd_numbers_to_15(self):
        output = self.run_exercise("15\n")
        expected_output = "1 3 5 7 9 11 13 15\n"
        self.assertEqual(output, expected_output)

    def test_odd_numbers_to_8(self):
        output = self.run_exercise("8\n")
        expected_output = "1 3 5 7\n"
        self.assertEqual(output, expected_output)

    def test_odd_numbers_to_5(self):
        output = self.run_exercise("5\n")
        expected_output = "1 3 5\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
