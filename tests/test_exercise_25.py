import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise25(CustomTestCase):

    def test_loop_usage(self):
        """
        The program should use a 'for' or 'while' loop to solve the exercise.
        """

        self.assertUsesLoops()

    def test_no_list_usage(self):
        """
        The program should not use a list to solve the exercise.
        """

        self.assertNotUsesList()

    def test_not_string_conversion(self):
        """
        The program should not convert the input to a string.
        """

        self.assertNotUseStringSlice()

    def test_car_distance(self):
        """
        The program should determine the number of days it takes for a car to cover a distance greater than `t` km, where the car covers `d` km on the first day and increases its distance by 10% each day.
        """

        inputs = ["10", "100"]
        output = self.run_exercise(inputs)
        expected_output = "114.36 km, 8 days\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_car_distance_2(self):
        """
        The program should determine the number of days it takes for a car to cover a distance greater than `t` km, where the car covers `d` km on the first day and increases its distance by 10% each day.
        """

        inputs = ["20", "50"]
        output = self.run_exercise(inputs)
        expected_output = "66.20 km, 3 days\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_car_distance_3(self):
        """
        The program should determine the number of days it takes for a car to cover a distance greater than `t` km, where the car covers `d` km on the first day and increases its distance by 10% each day.
        """

        inputs = ["5", "25"]
        output = self.run_exercise(inputs)
        expected_output = "30.53 km, 5 days\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_car_distance_4(self):
        """
        The program should determine the number of days it takes for a car to cover a distance greater than `t` km, where the car covers `d` km on the first day and increases its distance by 10% each day.
        """

        inputs = ["1", "10"]
        output = self.run_exercise(inputs)
        expected_output = "11.44 km, 8 days\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_car_distance_5(self):
        """
        The program should determine the number of days it takes for a car to cover a distance greater than `t` km, where the car covers `d` km on the first day and increases its distance by 10% each day.
        """

        inputs = ["50", "100"]
        output = self.run_exercise(inputs)
        expected_output = "105.00 km, 2 days\n"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs) 


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
