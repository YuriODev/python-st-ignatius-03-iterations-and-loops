
import unittest
import subprocess
import os
import ast

class TestExercise38(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_38.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_even_difference_true(self):
        output = self.run_exercise("2134389\n")
        self.assertIn("True", output)

    def test_even_difference_false(self):
        output = self.run_exercise("1234\n")
        self.assertIn("False", output)

    def test_even_difference_true_2(self):
        output = self.run_exercise("111111\n")
        self.assertIn("True", output)

    def test_even_difference_false_2(self):
        output = self.run_exercise("123456789\n")
        self.assertIn("True", output)

    def check_list_usage(self):
        with open("exercise_38.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_38.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)

    def check_str_in_usage(self):
        with open("exercise_38.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("in", code)

    def test_no_str_in_usage(self):
        with open("exercise_38.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("in", code)

    def check_str_function_usage(self):
        with open("exercise_38.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("str", code)


if __name__ == '__main__':
    unittest.main()
