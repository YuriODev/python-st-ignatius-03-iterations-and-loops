
import unittest
import subprocess
import os
import ast

class TestExercise29(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_29.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_sum_of_squares_until_zero(self):
        output = self.run_exercise("1\n2\n3\n4\n-4\n-3\n-2\n-1\n")
        self.assertEqual(int(output.strip()), 30)

    def test_sum_of_squares_until_zero_2(self):
        output = self.run_exercise("3\n4\n5\n-5\n-4\n-3\n")
        self.assertEqual(int(output.strip()), 50)

    def chek_list_usage(self):
        with open("exercise_29.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_29.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)

if __name__ == '__main__':
    unittest.main()
