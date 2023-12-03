import numpy as np

def reverse_zigzag_transform(_1d_array, N):
    """
    Return 2d block (N*N) from the 1d array zigzag-traversed
    :param _1d_array: 1d array (N*N)
    :param N: size of block
    :return: 2d block (N*N)
    """
    zigzag_indices = [(i,j) for i in range(N) for j in range(N)]
    zigzag_indices.sort(key = lambda x: (x[0]+ x[1], x[1]) if (x[0]+x[1])%2 == 0 else (x[0]+x[1], x[0]))

    block = np.zeros((N,N))

    for i,zigzag_index in enumerate(zigzag_indices):
        block[zigzag_index[0], zigzag_index[1]] = _1d_array[i]

    return block