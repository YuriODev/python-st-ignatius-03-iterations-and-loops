
import unittest
import subprocess
import os

class TestExercise22(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_22.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_number_pattern_138945(self):
        output = self.run_exercise("138945\n")
        expected_output = "13894\n1389\n138\n13\n1\n"
        self.assertEqual(output, expected_output)

    def test_number_pattern_123456(self):
        output = self.run_exercise("123456\n")
        expected_output = "12345\n1234\n123\n12\n1\n"
        self.assertEqual(output, expected_output)

    def test_number_pattern_987654(self):
        output = self.run_exercise("987654\n")
        expected_output = "98765\n9876\n987\n98\n9\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
