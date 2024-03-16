
import unittest
import subprocess
import os
import ast

class TestExercise40(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_40.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_fibonacci_sequence_to_50(self):
        output = self.run_exercise("50\n")
        expected_sequence = "1 1 2 3 5 8 13 21 34"
        self.assertIn(expected_sequence, output)

    def test_fibonacci_sequence_to_100(self):
        output = self.run_exercise("100\n")
        expected_sequence = "1 1 2 3 5 8 13 21 34 55 89"
        self.assertIn(expected_sequence, output)

    def test_fibonacci_sequence_to_200(self):
        output = self.run_exercise("200\n")
        expected_sequence = "1 1 2 3 5 8 13 21 34 55 89 144"
        self.assertIn(expected_sequence, output)

    def test_fibonacci_sequence_to_5(self):
        output = self.run_exercise("5\n")
        expected_sequence = "1 1 2 3 5"
        self.assertIn(expected_sequence, output)

    def test_fibonacci_sequence_to_10(self):
        output = self.run_exercise("10\n")
        expected_sequence = "1 1 2 3 5 8"
        self.assertIn(expected_sequence, output)

    def chek_list_usage(self):
        with open("exercise_40.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_40.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
