import unittest
import subprocess
import os


class TestExercise3(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_3.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_sequence_to_25(self):
        output = self.run_exercise("25\n")
        expected_output = "20 21 22 23 24 25\n"
        self.assertEqual(output, expected_output)

    def test_sequence_to_30(self):
        output = self.run_exercise("30\n")
        expected_output = "20 21 22 23 24 25 26 27 28 29 30\n"
        self.assertEqual(output, expected_output)

    def test_sequence_to_20(self):
        output = self.run_exercise("20\n")
        expected_output = "20\n"
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
