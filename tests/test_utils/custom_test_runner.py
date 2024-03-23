import unittest
from .enhanced_string_io import StringIOWithWriteLn as StringIO


class CustomTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, stream=StringIO(), **kwargs)

    def run(self, test):
        result = super().run(test)
        self.report_test_results(result)
        return result

    def report_test_results(self, test_results):
        total_tests = test_results.testsRun
        failed_tests = len(test_results.failures) + len(test_results.errors)
        passed_tests = total_tests - failed_tests
        passed_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

        if failed_tests > 0:
            print(f"\x1b[6;30;41m Tests passed: {passed_tests}/{total_tests} ({passed_percentage:.2f}%) \x1b[0m")
            first_failure = test_results.failures[0] if test_results.failures else test_results.errors[0]
            failure_message = first_failure[1]
            index = failure_message.find("Failed test:")
            if index != -1:
                print(failure_message[index:])
            else:
                print(failure_message)
        else:
            print("\x1b[6;30;42m Success! Your code works as intended. \x1b[0m")
