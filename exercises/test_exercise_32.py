
import unittest
import subprocess
import os
import ast

class TestExercise32(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_32.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_car_speeds(self):
        output = self.run_exercise("3\n15\n25\n140\n")
        self.assertEqual(output.strip(), "125\n2")

    def test_car_speeds_2(self):
        output = self.run_exercise("5\n100\n110\n120\n130\n140\n")
        self.assertEqual(output.strip(), "40\n5")

    def test_car_speeds_3(self):
        output = self.run_exercise("4\n100\n90\n80\n70\n")
        self.assertEqual(output.strip(), "30\n0")

    def chek_list_usage(self):
        with open("exercise_32.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_32.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
