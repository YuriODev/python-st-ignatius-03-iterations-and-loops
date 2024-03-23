
import unittest
import subprocess
import os
import ast

class TestExercise34(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_34.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_number_pattern_5(self):
        output = self.run_exercise("5\n")
        expected_output = "1\n12\n123\n1234\n12345\n"
        self.assertEqual(output, expected_output)

    def test_number_pattern_3(self):
        output = self.run_exercise("3\n")
        expected_output = "1\n12\n123\n"
        self.assertEqual(output, expected_output)

    def test_number_pattern_7(self):
        output = self.run_exercise("7\n")
        expected_output = "1\n12\n123\n1234\n12345\n123456\n1234567\n"
        self.assertEqual(output, expected_output)

    def chek_list_usage(self):
        with open("exercise_34.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_34.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)

    def check_string_index_usage(self):
        with open("exercise_34.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) and node.value.id == 'number':
                    self.fail("String index usage found in the code.")


if __name__ == '__main__':
    unittest.main()
