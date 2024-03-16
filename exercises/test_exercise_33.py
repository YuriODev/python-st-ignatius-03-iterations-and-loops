
import unittest
import subprocess
import os
import ast


class TestExercise33(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_33.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_two_dimensional_table(self):
        output = self.run_exercise("5\n")
        expected_output = "0\t1\t1\t1\t1\n-1\t0\t1\t1\t1\n-1\t-1\t0\t1\t1\n-1\t-1\t-1\t0\t1\n-1\t-1\t-1\t-1\t0\n"
        self.assertEqual(output, expected_output)

    def test_two_dimensional_table_3(self):
        output = self.run_exercise("3\n")
        expected_output = "0\t1\t1\n-1\t0\t1\n-1\t-1\t0\n"
        self.assertEqual(output, expected_output)

    def test_two_dimensional_table_1(self):
        output = self.run_exercise("1\n")
        expected_output = "0\n"
        self.assertEqual(output, expected_output)

    def chek_list_usage(self):
        with open("exercise_33.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_33.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
