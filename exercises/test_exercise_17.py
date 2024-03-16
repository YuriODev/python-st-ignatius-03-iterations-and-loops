
import unittest
import subprocess
import os

class TestExercise17(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_17.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_number_pattern_6_3(self):
        output = self.run_exercise("6\n3\n")
        expected_output = "0\t0\t0\n1\t1\t1\n2\t2\t2\n3\t3\t3\n4\t4\t4\n5\t5\t5\n6\t6\t6\n"
        self.assertEqual(output, expected_output)

    def test_number_pattern_3_3(self):
        output = self.run_exercise("3\n3\n")
        expected_output = "0\t0\t0\n1\t1\t1\n2\t2\t2\n"
        self.assertEqual(output, expected_output)

    def test_number_pattern_3_7(self):
        output = self.run_exercise("3\n7\n")
        expected_output = "0\t0\t0\t0\t0\t0\t0\t0\n1\t1\t1\t1\t1\t1\t1\t1\n2\t2\t2\t2\t2\t2\t2\t2\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
