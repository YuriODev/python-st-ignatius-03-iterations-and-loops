import unittest
import subprocess
import os
import ast

class TestExercise41(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_41.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_fibonacci_sequence_number(self):
        output = self.run_exercise("9\\n")
        self.assertEqual(int(output.strip()), 34)

    def test_fibonacci_sequence_number_2(self):
        output = self.run_exercise("10\\n")
        self.assertEqual(int(output.strip()), 55)

    def test_fibonacci_sequence_number_3(self):
        output = self.run_exercise("11\\n")
        self.assertEqual(int(output.strip()), 89)

    def test_fibonacci_sequence_number_4(self):
        output = self.run_exercise("12\\n")
        self.assertEqual(int(output.strip()), 144)

    def test_fibonacci_sequence_number_5(self):
        output = self.run_exercise("13\\n")
        self.assertEqual(int(output.strip()), 233)

    def test_fibonacci_sequence_number_6(self):
        output = self.run_exercise("14\\n")
        self.assertEqual(int(output.strip()), 377)

    def chek_list_usage(self):
        with open("exercise_41.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_41.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
