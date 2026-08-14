import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x)
    e = np.pow(np.e, -x)
    return 1 / (1 + e)