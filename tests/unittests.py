import unittest
import numpy as np
from IPA import compute_lpp, get_z_of_x


class SimplexTestCase(unittest.TestCase):
    alpha = .5
    accuracy = .001

    def testCase1(self):  # test method names begin with 'test'
        # ___________(data)______________ #

        correct_X = [6, 1, 0, 0]
        correct_Z = 7
        z_f = np.array([1, 1, 0, 0])
        cond = np.array([
            [2, 4, 1, 0],
            [1, 3, 0, -1],
        ])
        x_initial = [1/2, 7/2, 1, 2]

        # ------------(assertion)---------#
        ans = compute_lpp(z_f, cond, x_initial, self.alpha, self.accuracy)
        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z, 2)
        [self.assertAlmostEqual(entry, correct_X[idx], places=2) for idx, entry in enumerate(ans)]

    def testCase2(self):
        # ___________(data)______________ #

        correct_X = [0, 8, 20, 0, 0, 96]
        correct_Z = 400

        z_f = np.array([9, 10, 16, 0, 0, 0])
        cond = np.array([
            [18, 15, 12, 1, 0, 0],
            [6, 4, 8, 0, 1, 0],
            [5, 3, 3, 0, 0, 1]
        ])
        x_initial = [1, 1, 1, 315, 174, 169]
        # ------------(assertion)---------#

        ans = compute_lpp(z_f, cond, x_initial, self.alpha, self.accuracy)
        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z, places=2)
        [self.assertAlmostEqual(entry, correct_X[idx], places=2) for idx, entry in enumerate(ans)]

    def testCase3(self):
        # ___________(data)______________ #

        correct_X = [0, 8, 0]
        correct_Z = 16

        z_f = np.array([1, 2, 0])
        cond = np.array([
            [1, 1, 1],
        ])
        x_initial = [5/2, 7/2, 2]
        # ------------(assertion)---------#

        ans = compute_lpp(z_f, cond, x_initial, self.alpha, self.accuracy)
        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z, places=2)
        [self.assertAlmostEqual(entry, correct_X[idx], places=2) for idx, entry in enumerate(ans)]

    def testCase4(self):
        z_f = np.array([3, 1, 0, 0])  # Coefficients of the objective function
        cond = np.array([
            [2, 2, 1, 0],
            [1, 1, 0, 1]
        ])
        b_col = np.array([10, 6])
        x_initial = [2, 2, 2, 2]

        ans = compute_lpp(z_f, cond, x_initial, self.alpha, self.accuracy)

        correct_X = [5, 0, 0, 1]
        correct_Z = 15

        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z, places=2)
        [self.assertAlmostEqual(entry, correct_X[idx], places=2) for idx, entry in enumerate(ans)]

    def testCaseAlternativeOptima(self):
        z_f = np.array([2, 4, 0, 0])
        cond = np.array([
            [1, 2, 1, 0],
            [1, 1, 0, 1],
        ])
        b_col = np.array([5, 4])
        x_initial = [1, 1, 2, 2]

        correct_Z = 10
        correct_X = [3, 1, 0, 0]

        ans = compute_lpp(z_f, cond, x_initial, self.alpha, self.accuracy)
        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z, places=2)
        # [self.assertAlmostEqual(entry, correct_X[idx]) for idx, entry in enumerate(ans)]


def run_tests():
    unittest.main()


if __name__ == '__main__':
    unittest.main()
