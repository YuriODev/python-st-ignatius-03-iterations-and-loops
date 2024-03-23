
# ## Exercise 52: Odd Numbers - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

# **Problem:** Two numbers `a` and `b` are entered. Print all odd numbers from the interval from `a` to `b` (b ≤ a). Write a program without using a branching instruction.

# ### Input:

# - Two integers `a` and `b` (a ≥ b).

# ### Output:

# - A sequence of odd numbers from the interval from `a` to `b`.

# ### Examples:

# | No. | Inputs | Outputs |
# | --- | ------ | ------- |
# | 1   | 10<br>1 | 9 7 5 3 1 |
# | 2   | 20<br>1 | 19 17 15 13 11 9 7 5 3 1 |
# | 3   | 30<br>1 | 29 27 25 23 21 19 17 15 13 11 9 7 5 3 1 |

# ### Note:

# The problem tests the ability to use loops to print a sequence of numbers.

import unittest
import subprocess
import os
import ast


class TestExercise52(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_52.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_odd_numbers_10_1(self):
        output = self.run_exercise("10\n1\n")
        self.assertEqual(output.strip(), "9 7 5 3 1")

    def test_odd_numbers_20_1(self):
        output = self.run_exercise("20\n1\n")
        self.assertEqual(output.strip(), "19 17 15 13 11 9 7 5 3 1")

    def test_odd_numbers_30_1(self):
        output = self.run_exercise("30\n1\n")
        self.assertEqual(output.strip(), "29 27 25 23 21 19 17 15 13 11 9 7 5 3 1")

    def check_if_usage(self):
        with open("exercise_52.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("if", code)

    def check_list_usage(self):
        with open("exercise_52.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_str_usage(self):
        with open("exercise_52.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("str", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
