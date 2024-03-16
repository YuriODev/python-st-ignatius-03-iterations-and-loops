
import unittest
import subprocess
import os

class TestExercise34(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_34.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_number_pattern(self):
        output = self.run_exercise("5\n")
        expected_output = "1\n12\n123\n1234\n12345\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
