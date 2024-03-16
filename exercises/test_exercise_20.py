
import unittest
import subprocess
import os
import ast

class TestExercise20(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_20.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_odd_numbers_to_15(self):
        output = self.run_exercise("15\n")
        expected_output = "1 3 5 7 9 11 13 15\n"
        self.assertEqual(output, expected_output)

    def test_odd_numbers_to_8(self):
        output = self.run_exercise("8\n")
        expected_output = "1 3 5 7\n"
        self.assertEqual(output, expected_output)

    def test_odd_numbers_to_5(self):
        output = self.run_exercise("5\n")
        expected_output = "1 3 5\n"
        self.assertEqual(output, expected_output)

    def check_if_usage(self):
        with open("exercise_20.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.If):
                    self.fail("If usage found in the code.")

    def chek_list_usage(self):
        with open("exercise_20.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_20.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
