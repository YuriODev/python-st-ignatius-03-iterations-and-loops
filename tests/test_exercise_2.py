import unittest
import subprocess
import os


class TestExercise2(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_2.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_m_times_n_10_5(self):
        output = self.run_exercise("10\n5\n")
        expected_output = "10 10 10 10 10 \n"
        self.assertIn(expected_output, output)

    def test_m_times_n_3_3(self):
        output = self.run_exercise("3\n3\n")
        expected_output = "3 3 3 \n"
        self.assertIn(expected_output, output)

    def test_m_times_n_7_1(self):
        output = self.run_exercise("7\n1\n")
        expected_output = "7\n"
        self.assertIn(expected_output, output)


if __name__ == '__main__':
    unittest.main()
