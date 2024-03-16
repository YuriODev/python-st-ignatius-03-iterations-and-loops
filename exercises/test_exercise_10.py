
import unittest
import subprocess
import os

class TestExercise10(unittest.TestCase):
    def run_exercise(self, input_value):
        exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_10.py")
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_pound_to_kg_table_5(self):
        output = self.run_exercise("5\n")
        expected_output = "1 0.45\n2 0.91\n3 1.36\n4 1.81\n5 2.27\n"
        self.assertEqual(output, expected_output)

    def test_pound_to_kg_table_3(self):
        output = self.run_exercise("3\n")
        expected_output = "1 0.45\n2 0.91\n3 1.36\n"
        self.assertEqual(output, expected_output)

    def test_pound_to_kg_table_7(self):
        output = self.run_exercise("7\n")
        expected_output = "1 0.45\n2 0.91\n3 1.36\n4 1.81\n5 2.27\n6 2.72\n7 3.18\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
