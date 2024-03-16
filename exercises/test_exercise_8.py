
import unittest
import subprocess
import os
import ast


class TestExercise8(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_8.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_even_numbers_10(self):
        output = self.run_exercise("10\n")
        expected_output = "2 4 6 8 10\n"
        self.assertEqual(output, expected_output)

    def test_even_numbers_7(self):
        output = self.run_exercise("7\n")
        expected_output = "2 4 6\n"
        self.assertEqual(output, expected_output)

    def test_even_numbers_20(self):
        output = self.run_exercise("20\n")
        expected_output = "2 4 6 8 10 12 14 16 18 20\n"
        self.assertEqual(output, expected_output)

    def test_contains_continue(self):
        with open("exercise_8.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.Continue):
                    break
            else:
                self.fail("No continue statement found in the code.")

if __name__ == '__main__':
    unittest.main()
