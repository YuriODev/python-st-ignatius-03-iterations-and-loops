
import unittest
import subprocess
import os
import ast

class TestExercise24(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_24.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_even_elements_sequence(self):
        output = self.run_exercise("3\n6\n9\n8\n0\n")
        self.assertEqual(int(output.strip()), 2)

    def test_odd_elements_sequence(self):
        output = self.run_exercise("3\n6\n9\n8\n7\n0\n")
        self.assertEqual(int(output.strip()), 3)

    def chek_list_usage(self):
        with open("exercise_24.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_24.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
