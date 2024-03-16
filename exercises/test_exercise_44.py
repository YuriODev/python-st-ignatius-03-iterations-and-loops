import unittest
import subprocess
import os


class TestExercise44(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_44.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_index_of_largest_element(self):
        output = self.run_exercise("4\\n2\\n6\\n9\\n5\\n0\\n")
        self.assertEqual(int(output.strip()), 3)


if __name__ == '__main__':
    unittest.main()
