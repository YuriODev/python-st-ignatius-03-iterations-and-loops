import unittest
import subprocess
import os
import ast


class TestExercise45(unittest.TestCase):
    def run_exercise(self, input_values):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_45.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_values, text=True, universal_newlines=True)

    def test_sign_changes(self):
        output = self.run_exercise("-5\\n-3\\n10\\n6\\n-4\\n7\\n-1\\n0\\n")
        self.assertEqual(int(output.strip()), 4)

    def test_no_sign_changes(self):
        output = self.run_exercise("5\\n3\\n10\\n6\\n4\\n7\\n1\\n0\\n")
        self.assertEqual(int(output.strip()), 0)

    def test_sign_changes_2(self):
        output = self.run_exercise("5\\n3\\n10\\n6\\n-4\\n7\\n1\\n0\\n")
        self.assertEqual(int(output.strip()), 3)

    def test_sign_changes_3(self):
        output = self.run_exercise("-5\\n3\\n10\\n6\\n-4\\n7\\n1\\n0\\n")
        self.assertEqual(int(output.strip()), 3)

    def test_sign_changes_4(self):
        output = self.run_exercise("-5\\n-3\\n10\\n6\\n4\\n7\\n1\\n0\\n")
        self.assertEqual(int(output.strip()), 5)

    def test_sign_changes_5(self):
        output = self.run_exercise("-5\\n-3\\n-10\\n-6\\n-4\\n-7\\n-1\\n0\\n")
        self.assertEqual(int(output.strip()), 0)

    def chek_list_usage(self):
        with open("exercise_45.py", "r") as source_code:
            tree = ast.parse(source_code.read())
            for node in ast.walk(tree):
                if isinstance(node, (ast.List, ast.ListComp)):
                    self.fail("List usage found in the code.")
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'list':
                    self.fail("List usage found in the code.")

    def test_no_list_usage(self):
        with open("exercise_45.py", "r") as source_code:
            code = source_code.read()
            self.assertNotIn("list", code)
            self.assertNotIn("[", code)
            self.assertNotIn("]", code)


if __name__ == '__main__':
    unittest.main()
