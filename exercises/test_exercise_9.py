
import unittest
import subprocess
import os
import ast


class TestExercise9(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_9.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_multiples_of_2_between_1_and_10(self):
        output = self.run_exercise("1\n10\n2\n")
        expected_output = "2 4 6 8 10\n"
        self.assertEqual(output, expected_output)

    def test_multiples_of_3_between_3_and_15(self):
        output = self.run_exercise("3\n15\n3\n")
        expected_output = "3 6 9 12 15\n"
        self.assertEqual(output, expected_output)

    def test_multiples_of_5_between_5_and_20(self):
        output = self.run_exercise("5\n20\n5\n")
        expected_output = "5 10 15 20\n"
        self.assertEqual(output, expected_output)

    # Check if max function was used. It's not allowed and write a message to the user
    def test_if_max_function_was_used(self):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_9.py")
        with open(exercise_file_path, 'r') as file:
            file_content = file.read()
            self.assertNotIn("max(", file_content, "You should not use the max function in your solution")


if __name__ == '__main__':
    unittest.main()
