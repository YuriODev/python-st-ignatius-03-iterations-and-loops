# ## Exercise 51: Three Identical Digits - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

# **Problem:** Two four-digit numbers `a` and `b` are entered. Print all four-digit numbers in the interval from `a` to `b` that contain only three identical digits.

# ### Input:

# - Two four-digit numbers `a` and `b`.

# ### Output:

# - A sequence of four-digit numbers in the interval from `a` to `b` that contain only three identical digits.

# ### Examples:

# | No. | Inputs | Outputs |
# | --- | ------ | ------- |
# | 1   | 1400<br>1600 | 1411 1444 1511 1555 |
# | 2   | 1000<br>2000 | 1111 1222 1333 1444 1555 1666 1777 1888 1999 |
# | 3   | 2000<br>3000 | 2002 2111 2222 2333 2444 2555 2666 2777 2888 2999 |

import unittest
import subprocess
import os
import ast


class TestExercise51(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_51.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_three_identical_digits_1400_1600(self):
        output = self.run_exercise("1400\n1600\n")
        self.assertEqual(output.strip(), "1411 1444 1511 1555")

    def test_three_identical_digits_1000_2000(self):
        output = self.run_exercise("1000\n2000\n")
        self.assertEqual(output.strip(), "1111 1222 1333 1444 1555 1666 1777 1888 1999")

    def test_three_identical_digits_2000_3000(self):
        output = self.run_exercise("2000\n3000\n")
        self.assertEqual(output.strip(), "2002 2111 2222 2333 2444 2555 2666 2777 2888 2999")

    def check_list_usage(self):
        with open("exercise_51.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_str_usage(self):
        with open("exercise_51.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("str", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
