
import unittest
import subprocess
import os

class TestExercise4(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_4.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_number_of_hashes_5(self):
        output = self.run_exercise("5\n")
        expected_output = "1 #\n2 ##\n3 ###\n4 ####\n5 #####\n"
        self.assertEqual(output, expected_output)

    def test_number_of_hashes_3(self):
        output = self.run_exercise("3\n")
        expected_output = "1 #\n2 ##\n3 ###\n"
        self.assertEqual(output, expected_output)

    def test_number_of_hashes_7(self):
        output = self.run_exercise("7\n")
        expected_output = "1 #\n2 ##\n3 ###\n4 ####\n5 #####\n6 ######\n7 #######\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
