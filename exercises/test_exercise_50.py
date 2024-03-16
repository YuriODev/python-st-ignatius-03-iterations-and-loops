import unittest
import subprocess
import os
import ast


class TestExercise50(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_50.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_palindromes_10(self):
        output = self.run_exercise("10\n")
        self.assertEqual(int(output.strip()), 9)

    def test_palindromes_50(self):
        output = self.run_exercise("50\n")
        self.assertEqual(int(output.strip()), 13)

    def test_palindromes_100(self):
        output = self.run_exercise("100\n")
        self.assertEqual(int(output.strip()), 18)

    def test_palindromes_200(self):
        output = self.run_exercise("200\n")
        self.assertEqual(int(output.strip()), 27)

    def check_list_usage(self):
        with open("exercise_50.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_50.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)

    def test_reverse_usage(self):
        with open("exercise_50.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("reverse", code)

    def test_string_slice_usage_reverse(self):
        with open("exercise_50.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("[::-1]", code)


if __name__ == '__main__':
    unittest.main()
