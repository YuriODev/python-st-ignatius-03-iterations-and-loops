
import unittest
import subprocess
import os
import ast

class TestExercise39(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_39.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_sum_of_digits_negative(self):
        output = self.run_exercise("-123\n")
        self.assertEqual(int(output.strip()), 6)

    def test_sum_of_digits_positive(self):
        output = self.run_exercise("123\n")
        self.assertEqual(int(output.strip()), 6)

    def test_sum_of_digits_zero(self):
        output = self.run_exercise("0\n")
        self.assertEqual(int(output.strip()), 0)

    def test_sum_of_digits_single_digit(self):
        output = self.run_exercise("5\n")
        self.assertEqual(int(output.strip()), 5)

    def test_sum_of_digits_single_digit_negative(self):
        output = self.run_exercise("-5\n")
        self.assertEqual(int(output.strip()), 5)

    def chek_list_usage(self):
        with open("exercise_39.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_39.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)

    def check_sum_function_usage(self):
        with open("exercise_39.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    self.fail("sum function usage found in the code.")

    def test_no_sum_function_usage(self):
        with open("exercise_39.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("sum(", code)


if __name__ == '__main__':
    unittest.main()
