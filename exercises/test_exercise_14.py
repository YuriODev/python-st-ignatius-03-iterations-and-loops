
import unittest
import subprocess
import os
import ast

class TestExercise14(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_14.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_count_of_zeros(self):
        output = self.run_exercise("4\n0\n23\n11\n0\n")
        self.assertEqual(int(output.strip()), 2)

    def test_all_zeros(self):
        output = self.run_exercise("3\n0\n0\n0\n")
        self.assertEqual(int(output.strip()), 3)

    def test_no_zeros(self):
        output = self.run_exercise("5\n1\n2\n3\n4\n5\n")
        self.assertEqual(int(output.strip()), 0)

    def test_no_list_usage(self):
        with open("exercise_14.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

if __name__ == '__main__':
    unittest.main()
