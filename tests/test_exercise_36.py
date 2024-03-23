
import unittest
import subprocess
import os
import ast

class TestExercise36(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_36.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_gcd(self):
        output = self.run_exercise("8\n2\n")
        self.assertEqual(int(output.strip()), 2)

    def test_gcd_2(self):
        output = self.run_exercise("12\n8\n")
        self.assertEqual(int(output.strip()), 4)

    def test_gcd_3(self):
        output = self.run_exercise("100\n25\n")
        self.assertEqual(int(output.strip()), 25)

    def check_math_module_usage(self):
        with open("exercise_36.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.Import) and node.names[0].name == 'math':
                    self.fail("math module usage found in the code.")
                elif isinstance(node, ast.ImportFrom) and node.module == 'math':
                    self.fail("math module usage found in the code.")

    def test_no_math_module_usage(self):
        with open("exercise_36.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("math", code)

    def check_gcd_function_usage(self):
        with open("exercise_36.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == 'gcd':
                    self.fail("gcd function usage found in the code.")

    def test_no_gcd_function_usage(self):
        with open("exercise_36.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("gcd", code)

    def check_module_usage(self):
        with open("exercise_36.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("import", code)
            self.assertNotIn("from", code)

    def check_modulo_operator_usage(self):
        with open("exercise_36.py", "r") as source_code:
            code = source_code.read()
            self.assertIn("%", code)

if __name__ == '__main__':
    unittest.main()
