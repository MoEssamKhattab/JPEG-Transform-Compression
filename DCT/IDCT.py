from .IDCT_Basis import IDCT_Basis
import numpy as np

def IDCT(C):
    """
    Return the IDCT of a block
    :param C: numpy array of the block
    :return: IDCT of C
    """
    N = len(C)
    A = np.zeros((N,N))

    for x in range(N):
        for y in range(N):
            basis = IDCT_Basis(x,y,N)
            A[x][y] = np.sum(np.multiply(C, basis))
    return np.round(A)
