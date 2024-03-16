
import unittest
import subprocess
import os
import ast

class TestExercise37(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_37.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_division_without_division(self):
        output = self.run_exercise("16\n5\n")
        results = output.strip().split()
        self.assertEqual(results, ['3', '1'])

    def test_division_without_division_2(self):
        output = self.run_exercise("100\n3\n")
        results = output.strip().split()
        self.assertEqual(results, ['33', '1'])

    def test_division_without_division_3(self):
        output = self.run_exercise("100\n25\n")
        results = output.strip().split()
        self.assertEqual(results, ['4', '0'])

    def check_module_usage(self):
        with open("exercise_37.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("import", code)
            self.assertNotIn("from", code)

    def check_division_operator_usage(self):
        with open("exercise_37.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("/", code)


if __name__ == '__main__':
    unittest.main()
