
import unittest
import subprocess
import os

class TestExercise16(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_16.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_staircase_pattern_4(self):
        output = self.run_exercise("4\n")
        expected_output = "   #\n  ##\n ###\n####\n"
        self.assertEqual(output, expected_output)

    def test_staircase_pattern_3(self):
        output = self.run_exercise("3\n")
        expected_output = "  #\n ##\n###\n"
        self.assertEqual(output, expected_output)

    def test_staircase_pattern_7(self):
        output = self.run_exercise("7\n")
        expected_output = "     #\n    ##\n   ###\n  ####\n #####\n######\n#######\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
