import unittest
import subprocess
import os


class TestExercise1(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_1.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_countdown_5(self):
        output = self.run_exercise("5\n")
        expected_output = "5\n4\n3\n2\n1\nStart!\n"
        self.assertIn(output, expected_output)

    def test_countdown_3(self):
        output = self.run_exercise("3\n")
        expected_output = "3\n2\n1\nStart!\n"
        self.assertIn(output, expected_output)

    def test_countdown_1(self):
        output = self.run_exercise("1\n")
        expected_output = "1\nStart!\n"
        self.assertIn(output, expected_output)


if __name__ == '__main__':
    unittest.main()
