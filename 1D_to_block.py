import numpy as np


def one_d_to_block(flattened, N):
    """
        Reconstruct a square block from a flattened 1D vector.

        Parameters:
        - flattened (list or numpy.ndarray): 1D vector representing the flattened block.
        - N (int): Size of the square block (N x N).

        Returns:
        - numpy.ndarray: 2D array representing the reconstructed square block.

        The function reconstructs a square block by extracting diagonals from the
        flattened vector. It processes both forward and backward diagonals,
        alternating between them.
        array([[ 1.,  2.,  3.,  4.],
               [ 5.,  6.,  7.,  8.],
               [ 9., 10., 11., 12.],
               [13., 14., 15., 16.]])
        """

    block = np.zeros((N, N))
    current_mode = 0
    idx = 0
    for i in range(N):
        idx = get_diagonal(block,idx,current_mode,i,flattened)
        current_mode = 1 ^ current_mode
    current_mode = (N % 2 == 0)
    block = np.rot90(np.rot90(block))
    for i in reversed(range(N - 1)):
        idx = get_diagonal(block,idx,current_mode,i,flattened)
        current_mode = 1 ^ current_mode
    block = np.rot90(np.rot90(block))
    return block


def get_diagonal(block,idx,current_mode,i,flattened):
    if current_mode == 0:
        for j in range(i + 1):
            block[i - j][j] = flattened[idx]
            idx += 1
    else:
        for j in range(i + 1):
            block[j][i - j] = flattened[idx]
            idx += 1
    return idx


print(one_d_to_block([1, 2, 5, 9, 6, 3, 4, 7, 10, 13, 14, 11, 8, 12, 15, 16], 4))
