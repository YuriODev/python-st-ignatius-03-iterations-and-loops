import unittest
import subprocess
import os
import ast


class TestExercise49(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_49.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_palindromes_1400_2200(self):
        output = self.run_exercise("1400\n2200\n")
        self.assertEqual(output.strip(), "1441 1551 1661 1771 1881 1991 2002 2112")

    def test_palindromes_1000_2000(self):
        output = self.run_exercise("1000\n2000\n")
        self.assertEqual(output.strip(), "1001 1111 1221 1331 1441 1551 1661 1771 1881 1991")

    def test_palindromes_2000_3000(self):
        output = self.run_exercise("2000\n3000\n")
        self.assertEqual(output.strip(), "2002 2112 2222 2332 2442 2552 2662 2772 2882 2992")

    def check_list_usage(self):
        with open("exercise_49.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_49.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)

    def test_reverse_usage(self):
        with open("exercise_49.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("reverse", code)

    def test_string_slice_usage_reverse(self):
        with open("exercise_49.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("[::-1]", code)


if __name__ == '__main__':
    unittest.main()
