
import unittest
import subprocess
import os

class TestExercise28(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_28.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_product_of_7_and_8(self):
        output = self.run_exercise("7\n8\n")
        self.assertEqual(int(output.strip()), 56)

if __name__ == '__main__':
    unittest.main()
