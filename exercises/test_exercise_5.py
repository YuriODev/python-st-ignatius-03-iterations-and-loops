
import unittest
import subprocess
import os

class TestExercise5(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_5.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_sum_of_integers_100(self):
        output = self.run_exercise("100\n")
        expected_output = "5050\n"
        self.assertEqual(output, expected_output)

    def test_sum_of_integers_16(self):
        output = self.run_exercise("16\n")
        expected_output = "136\n"
        self.assertEqual(output, expected_output)

    def test_sum_of_integers_1(self):
        output = self.run_exercise("1\n")
        expected_output = "1\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
