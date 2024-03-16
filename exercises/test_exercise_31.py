
import unittest
import subprocess
import os
import ast

class TestExercise31(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_31.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_lowest_temperature_below_minus_15(self):
        output = self.run_exercise("3\n-20\n2\n-18\n")
        self.assertIn("-20\nYes", output)

    def test_lowest_temperature_above_minus_15(self):
        output = self.run_exercise("3\n-14\n2\n-8\n")
        self.assertIn("-14\nNo", output)

    def test_lowest_temperature_at_minus_15(self):
        output = self.run_exercise("3\n-15\n2\n-18\n")
        self.assertIn("-15\nYes", output)

    def chek_list_usage(self):
        with open("exercise_31.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_31.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
