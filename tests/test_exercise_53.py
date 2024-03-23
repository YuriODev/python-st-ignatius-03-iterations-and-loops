# ## Exercise 53: Even Numbers - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

# **Problem:** Two numbers `a` and `b` are entered. Print all even numbers from the interval from `a` to `b` (a ≤ b). Write a program without using a branching instruction.

# ### Input:

# - Two integers `a` and `b` (a ≤ b).

# ### Output:

# - A sequence of even numbers from the interval from `a` to `b`.

# ### Examples:

# | No. | Inputs | Outputs |
# | --- | ------ | ------- |
# | 1   | 1<br>20 | 2 4 6 8 10 12 14 16 18 20 |
# | 2   | 1<br>30 | 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 |
# | 3   | 1<br>40 | 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 |


import unittest
import subprocess
import os
import ast


class TestExercise52(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_53.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_even_numbers_1_20(self):
        output = self.run_exercise("1\n20\n")
        self.assertEqual(output.strip(), "2 4 6 8 10 12 14 16 18 20")

    def test_even_numbers_1_30(self):
        output = self.run_exercise("1\n30\n")
        self.assertEqual(output.strip(), "2 4 6 8 10 12 14 16 18 20 22 24 26 28 30")

    def test_even_numbers_1_40(self):
        output = self.run_exercise("1\n40\n")
        self.assertEqual(output.strip(), "2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40")

    def check_if_usage(self):
        with open("exercise_53.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("if", code)

    def check_list_usage(self):
        with open("exercise_53.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_str_usage(self):
        with open("exercise_53.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("str", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
