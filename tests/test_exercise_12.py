
import unittest
import subprocess
import os

class TestExercise12(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_12.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_sum_of_three_digit_numbers_divisible_by_125(self):
        output = self.run_exercise("125\n")
        self.assertEqual(int(output.strip()), 3500)

    def test_sum_of_three_digit_numbers_divisible_by_440(self):
        output = self.run_exercise("440\n")
        self.assertEqual(int(output.strip()), 1320)

    def test_sum_of_three_digit_numbers_divisible_by_600(self):
        output = self.run_exercise("600\n")
        self.assertEqual(int(output.strip()), 600)

if __name__ == '__main__':
    unittest.main()
