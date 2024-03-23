# import io
# import unittest
# import subprocess
# import os


# class TestOutputFormatter:
#     @staticmethod
#     def get_failure_details_in_table(input_value: list, expected_output, actual_output) -> str:

#         # Convert the input list into a string
#         input_value = '\n'.join(input_value)

#         # ANSI escape code for yellow
#         yellow_start = "\x1b[38;5;208m"
#         yellow_end = "\x1b[0m"

#         # Print the "Failed test:" message
#         output = f"\n{yellow_start}Failed test:{yellow_end}\n"

#         # Find the longest output list for proper table formatting
#         max_lines = max(len(expected_output), len(actual_output))
#         max_length = max([len(input_value)] + [len(line) for line in expected_output + actual_output])
#         column_width = max_length + 2  # padding

#         # Preparing the table border based on the longest content
#         table_width = 3 * column_width + 9  # including padding and separators
#         divider = yellow_start + "+" + "-" * (table_width - 1) + "+" + yellow_end

#         # Printing the table headers and top border
#         output += divider + "\n"
#         header = f"| {'Input'.ljust(column_width)} | {'Expected Output'.ljust(column_width)} | {'Actual Output'.ljust(column_width)} |"
#         output += yellow_start + header + yellow_end + "\n"
#         output += divider + "\n"

#         # Iterating over the maximum number of lines and printing each row
#         for i in range(max_lines):
#             exp = expected_output[i] if i < len(expected_output) else ""
#             act = actual_output[i] if i < len(actual_output) else ""
#             if i == 0:
#                 row = f"| {input_value.ljust(column_width)} | {exp.ljust(column_width)} | {act.ljust(column_width)} |"
#             else:
#                 row = f"| {''.ljust(column_width)} | {exp.ljust(column_width)} | {act.ljust(column_width)} |"
#             output += yellow_start + row + yellow_end + "\n"

#         # Printing the bottom border
#         output += divider + "\n"

#         return output


# class CustomTestCase(unittest.TestCase):

#     @property
#     def exercise_file_name(self):
#         class_name = self.__class__.__name__
#         ex_number = class_name.split("TestExercise")[1]
#         return f"exercise_{ex_number}.py"
    
#     def run_exercise(self, inputs):
#             """Helper method to run the exercise script with the provided inputs and return its output."""
#             # The inputs list is joined into a single string, each separated by '\n'
#             input_value = '\n'.join(inputs) + '\n'
#             exercise_file_path = os.path.join(os.path.dirname(__file__), f"../exercises/{self.exercise_file_name}")
#             return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

#     def assertInCustom(self, expected, actual, input_value, msg=None):

#         """
#         Custom assertIn method to catch assertion errors and customize the error message.
#         """
#         try:
#             self.assertIn(expected, actual)
#         except AssertionError:
#             custom_message = TestOutputFormatter.get_failure_details_in_table(input_value, expected.split('\n'), actual.split('\n'))
#             if msg:
#                 custom_message += f"\nAdditional message: {msg}"
#             raise AssertionError(custom_message)


# class StringIOWithWriteLn(io.StringIO):
#     def writeln(self, *args):
#         self.write(args[0] if args else '')
#         self.write('\n')


# class CustomTestRunner(unittest.TextTestRunner):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, stream=StringIOWithWriteLn(), **kwargs)

#     def run(self, test):
#         result = super().run(test)
#         self.report_test_results(result)
#         return result

#     def report_test_results(self, test_results):
#         total_tests = test_results.testsRun
#         failed_tests = len(test_results.failures) + len(test_results.errors)
#         passed_tests = total_tests - failed_tests
#         passed_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

#         if failed_tests > 0:
#             print(f"\x1b[6;30;41m Tests passed: {passed_tests}/{total_tests} ({passed_percentage:.2f}%) \x1b[0m")
#             first_failure = test_results.failures[0] if test_results.failures else test_results.errors[0]
#             failure_message = first_failure[1]
#             index = failure_message.find("Failed test:")
#             if index != -1:
#                 print(failure_message[index:])
#             else:
#                 print(failure_message)
#         else:
#             print("\x1b[6;30;42m Success! Your code works as intended. \x1b[0m")


import unittest
from test_utils import CustomTestCase, CustomTestRunner


class TestExercise10(CustomTestCase):
    # def run_exercise(self, inputs):
    #     """Helper method to run the exercise script with the provided inputs and return its output."""
    #     # The inputs list is joined into a single string, each separated by '\n'
    #     input_value = '\n'.join(inputs) + '\n'
    #     exercise_file_path = os.path.join(os.path.dirname(__file__), "../exercise_10.py")
    #     return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_pound_to_kg_table_5(self):
        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "1 0.45\n2 0.91\n3 1.36\n4 1.81\n5 2.27\n"
        self.assertInCustom(expected=expected_output, actual=output, input_value=inputs)

    def test_pound_to_kg_table_3(self):
        inputs = ["3"]
        output = self.run_exercise(inputs)
        expected_output = "1 0.45\n2 0.91\n3 1.36\n"
        self.assertInCustom(expected=expected_output, actual=output, input_value=inputs)

    def test_pound_to_kg_table_7(self):
        inputs = ["7"]
        output = self.run_exercise(inputs)
        expected_output = "1 0.45\n2 0.91\n3 1.36\n4 1.81\n5 2.27\n6 2.72\n7 3.17\n"
        self.assertInCustom(expected=expected_output, actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
