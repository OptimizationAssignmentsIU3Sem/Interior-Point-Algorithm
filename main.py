import unittest

import numpy as np

from ipa_io import input_lpp, output_lpp, print_error
from IPA import compute_lpp, get_z_of_x
from simplex import simplex

# if you set TEST to true the standard input won't work, it will run only tests instead
TEST = False

if __name__ == "__main__":
    if TEST:
        unittest.main(module="tests")
    C, A, b, x_init, accuracy = input_lpp()
    try:
        # First we try it with simplex as in task 1
        print("\n\nUsing simplex method")
        result_for_simplex = simplex(C, A, b, accuracy)
        value = get_z_of_x(C, result_for_simplex)
        output_lpp(result_for_simplex, value)

        # Now we try alpha = 0.5
        result_for_a_0_5 = compute_lpp(C, A, x_init, .5, accuracy)
        value = get_z_of_x(C, result_for_a_0_5)

        print("\n\nIPA, With alpha = .5")
        output_lpp(result_for_a_0_5, value)

        # Now, as it was asked in the assignment, we set alpha = 0.9
        result_for_a_0_9 = compute_lpp(C, A, x_init, .9, accuracy)
        value = get_z_of_x(C, result_for_a_0_9)

        print("\n\nIPA, With alpha = .9")
        output_lpp(result_for_a_0_9, value)

    except ValueError as e:
        print_error(str(e))
