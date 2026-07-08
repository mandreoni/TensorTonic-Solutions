import numpy as np

E = 2.718281828459045


def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Convert and calculate
    x_arr = np.array(x)
    result = np.exp(-x_arr)
    tmp = 1 + result
    res = 1/tmp
    pass
    return res
