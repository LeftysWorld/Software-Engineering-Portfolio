###########
# Imports #
###########

import unittest
from Project_Euler.problem_sets.problem_16 import x_to_the_n_power, number_to_list


###################
# Testing Library #
###################

class TestProjectEuler(unittest.TestCase):
    def test_x_to_the_n_power(self):
        base = 2
        exponent = 3
        expected_res = 8
        res = x_to_the_n_power(base, exponent)

        self.assertEqual(expected_res, res)

    def test_number_to_list(self):
        n = 8
        expected_res = 8
        res = number_to_list(n)

        self.assertEqual(expected_res, res)


##################
# Test Functions #
##################

if __name__ == '__main__':
    unittest.main()
