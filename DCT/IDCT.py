from .DCT_Basis import DCT_Basis
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
            A[x][y] = np.sum(np.multiply(C, DCT_Basis(x,y,N)))
    
    #Denormalization
    A = A*16
    A[0,:] = A[0,:]/2
    A[:,0] = A[:,0]/2
    #A = np.round(A)
    
    return A