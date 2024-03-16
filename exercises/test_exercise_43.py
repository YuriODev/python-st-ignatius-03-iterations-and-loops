import unittest
import subprocess
import os


class TestExercise43(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_43.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_second_largest_element(self):
        output = self.run_exercise("1\\n4\\n3\\n2\\n0\\n")
        self.assertEqual(int(output.strip()), 3)


if __name__ == '__main__':
    unittest.main()
