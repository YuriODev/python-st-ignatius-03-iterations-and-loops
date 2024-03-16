
import unittest
import subprocess
import os

class TestExercise19(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_19.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_sum_of_squares_divisible_by_5(self):
        output = self.run_exercise("5\n")
        expected_numbers = [12, 13, 17, 18, 21, 24, 26, 29, 31, 34, 36, 39, 42, 43, 47, 48, 50, 55, 62, 63, 67, 68, 71, 74, 76, 79, 81, 84, 86, 89, 92, 93, 97, 98]
        output_numbers = list(map(int, output.strip().split(", ")))
        self.assertEqual(output_numbers, expected_numbers)

if __name__ == '__main__':
    unittest.main()
