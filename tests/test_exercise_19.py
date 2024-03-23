
import unittest
import subprocess
import os
import ast

class TestExercise19(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_19.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_sum_of_squares_divisible_by_5(self):
        output = self.run_exercise("5\n")
        expected_numbers = [12, 13, 17, 18, 21, 24, 26, 29, 31, 34, 36, 39, 42, 43, 47, 48, 50, 55, 62, 63, 67, 68, 71, 74, 76, 79, 81, 84, 86, 89, 92, 93, 97, 98]
        output_numbers = list(map(int, output.strip().split(", ")))
        self.assertEqual(output_numbers, expected_numbers)

    def test_sum_of_squares_divisible_by_7(self):
        output = self.run_exercise("7\n")
        expected_numbers = [70, 77]
        output_numbers = list(map(int, output.strip().split(", ")))
        self.assertEqual(output_numbers, expected_numbers)

    def test_sum_of_squares_divisible_by_188(self):
        output = self.run_exercise("188\n")
        expected_numbers = [99]
        output_numbers = list(map(int, output.strip().split(", ")))
        self.assertEqual(output_numbers, expected_numbers)

    def chek_list_usage(self):
        with open("exercise_19.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_19.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
