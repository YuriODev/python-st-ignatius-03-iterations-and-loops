
import unittest
import subprocess
import os

class TestExercise21(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_21.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_sum_of_factorials_3(self):
        output = self.run_exercise("3\n")
        self.assertEqual(int(output.strip()), 9)

    def test_sum_of_factorials_4(self):
        output = self.run_exercise("4\n")
        self.assertEqual(int(output.strip()), 33)

    def test_sum_of_factorials_5(self):
        output = self.run_exercise("5\n")
        self.assertEqual(int(output.strip()), 152)

if __name__ == '__main__':
    unittest.main()
