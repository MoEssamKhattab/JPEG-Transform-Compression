import numpy as np


def block_to_1d(block):
    """
        Convert a 2D square block into a 1D vector by extracting diagonals.

        Parameters:
        - block (numpy.ndarray): 2D square array representing a block of an image.

        Returns:
        - numpy.ndarray: 1D vector obtained by concatenating diagonals of the block.

        The function processes both forward and backward diagonals of the block,
        alternating between them.
        """

    current_mode = 0
    N, N = block.shape
    image_vector = np.array([])
    for i in range(N):
        image_vector = np.append(image_vector, get_diagonal(current_mode, block, i))
        current_mode = 1 ^ current_mode
    current_mode = (N % 2 == 0)
    block = np.rot90(np.rot90(block))
    for i in reversed(range(N - 1)):
        image_vector = np.append(image_vector, get_diagonal(current_mode, block, i))
        current_mode = 1 ^ current_mode

    return image_vector


def get_diagonal(current_mode, block, i):
    diagonal = np.array([])
    if current_mode == 0:
        for j in range(i + 1):
            diagonal = np.append(diagonal, block[i - j][j])
    else:
        for j in range(i + 1):
            diagonal = np.append(diagonal, block[j][i - j])
    return diagonal