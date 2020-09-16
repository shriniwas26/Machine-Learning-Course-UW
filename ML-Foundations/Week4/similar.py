import numpy as np


def to_array(space_separated_number_string):
    return [int(x) for x in space_separated_number_string.split()]


if __name__ == "__main__":
    a = to_array("1 3 2 1 2 1 1")
    a_hat = a / np.linalg.norm(a)
    docs = [
        [7, 0, 2, 1, 0, 0, 1],
        [1, 7, 0, 0, 2, 0, 1],
        [1, 0, 0, 0, 7, 1, 2],
        [0, 2, 0, 0, 7, 1, 1]
    ]

    for b in docs:
        b_hat = np.array(b) / np.linalg.norm(b)
        dotprod = np.dot(a_hat, b_hat)
        print("Vector {} has dotproduct {:.3f}".format(b, dotprod))
