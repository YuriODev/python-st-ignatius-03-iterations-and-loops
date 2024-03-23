# ## Exercise 47: Number of Palindromes - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

# **Problem:** Write a program to determine the number of palindromes that do not exceed `n`, where `n` is an integer entered by the user.

# ### Input:

# - An integer `n` (1 ≤ n ≤ 100000).

# ### Output:

# - A sequence of numbers representing the palindromes that do not exceed `n`.

# ### Examples:

# | No. | Inputs | Outputs |
# | --- | ------ | ------- |
# | 1   | 50 | 1 2 3 4 5 6 7 8 9 11 22 33 44 |
# | 2   | 100 | 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 |
# | 3   | 200 | 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 |


import unittest
import subprocess
import os
import ast


class TestExercise47(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_47.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_palindromes_50(self):
        output = self.run_exercise("50\n")
        self.assertEqual(output.strip(), "1 2 3 4 5 6 7 8 9 11 22 33 44")

    def test_palindromes_100(self):
        output = self.run_exercise("100\n")
        self.assertEqual(output.strip(), "1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99")

    def test_palindromes_200(self):
        output = self.run_exercise("200\n")
        self.assertEqual(output.strip(), "1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191")

    def test_palindromes_1000(self):
        output = self.run_exercise("1000\n")
        self.assertEqual(output.strip(), "1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212 222 232 242 252 262 272 282 292 303 313 323 333 343 353 363 373 383 393 404 414 424 434 444 454 464 474 484 494 505 515 525 535 545 555 565 575 585 595 606 616 626 636 646 656 666 676 686 696 707 717 727 737 747 757 767 777 787 797 808 818 828 838 848 858 868 878 888 898 909 919 929 939 949 959 969 979 989 999")

    def check_list_usage(self):
        with open("exercise_47.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_47.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)

    def test_reverse_usage(self):
        with open("exercise_47.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("reverse", code)

    def test_string_slice_usage_reverse(self):
        with open("exercise_47.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("[::-1]", code)


if __name__ == '__main__':
    unittest.main()
