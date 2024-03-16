
import unittest
import subprocess
import os
import ast

class TestExercise22(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_22.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_number_pattern_138945(self):
        output = self.run_exercise("138945\n")
        expected_output = "13894\n1389\n138\n13\n1\n"
        self.assertEqual(output, expected_output)

    def test_number_pattern_123456(self):
        output = self.run_exercise("123456\n")
        expected_output = "12345\n1234\n123\n12\n1\n"
        self.assertEqual(output, expected_output)

    def test_number_pattern_987654(self):
        output = self.run_exercise("987654\n")
        expected_output = "98765\n9876\n987\n98\n9\n"
        self.assertEqual(output, expected_output)

    def check_string_index_usage(self):
        with open("exercise_22.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) and node.value.id == 'number':
                    self.fail("String index usage found in the code.")

    def chek_list_usage(self):
        with open("exercise_22.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_22.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
