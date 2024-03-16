
import unittest
import subprocess
import os

class TestExercise32(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_32.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_car_speeds(self):
        output = self.run_exercise("3\n15\n25\n140\n")
        self.assertEqual(output.strip(), "125\n2")

if __name__ == '__main__':
    unittest.main()
