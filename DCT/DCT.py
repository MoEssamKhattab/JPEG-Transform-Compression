from .DCT_Basis import DCT_Basis
import numpy as np

def my_DCT(A):
    """
    Return the DCT of a block
    :param A: numpy array of the block
    :return: DCT of A
    """
    N = len(A)
    C = np.zeros((N,N))

    for u in range(N):
        for v in range(N):
            C[u,v] = sum(sum(np.multiply(A, DCT_Basis(u,v,N))))

    #Normalization
    C = C/16
    C[0,:] = C[0,:]/2
    C[:,0] = C[:,0]/2
    C = np.round(C)
    
    return C