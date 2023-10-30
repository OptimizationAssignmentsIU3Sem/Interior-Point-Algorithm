import numpy
import numpy as np
from numpy .linalg import norm


def get_z_of_x(z: np.array, x: np.array) -> float:
    return np.dot(z, x)


def compute_lpp(z: np.array, A: np.array, x_initial: np.array, alpha: float, accuracy: float) -> numpy.array:
    """
    This function computes maximum of a function with coefficients z, subject to given set
    of constraints A, from initial interior point x.

    :param alpha: learning rate
    :param x_initial: a point in feasible set
    :param A: matrix of constraints
    :param z: coefficients of z function
    :param accuracy: accuracy of the algorithm
    :return: optimal solution
    """

    dim = len(x_initial)
    i = 1
    x = x_initial

    while True:
        x_prev = x
        D = np.diag(x)
        A_tilda = np.dot(A, D)
        c_tilda = np.dot(D, z)

        I = np.eye(dim)

        # computing (A * A^T)^-1 (Means, A_tilda)
        F = np.dot(A_tilda, np.transpose(A_tilda))
        FI = np.linalg.inv(F)

        # finishing with calculation of P
        H = np.dot(np.transpose(A_tilda), FI)
        P = np.subtract(I, np.dot(H, A_tilda))

        cp = np.dot(P, c_tilda)
        nu = np.absolute(np.min(cp))
        x_tilda = np.add(np.ones(dim, float), (alpha / nu) * cp)
        x = np.dot(D, x_tilda)

        # print(x)
        i += 1
        if norm(np.subtract(x, x_prev), ord=4) < accuracy:
            print("did {} iterations".format(i))
            return x


if __name__ == "__main__":
    pass
