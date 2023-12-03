# Another implementation of the 2d block into 1d array

import numpy as np

def zigzag_transform(block, N):
    zigzag_indices = [(i,j) for i in range(N) for j in range(N)]
    zigzag_indices.sort(key = lambda x: (x[0], x[0]+x[1]) if (x[0]+x[1])%2 == 0 else (x[0]+x[1], x[1]))

    _1d_array = np.array(N*N)

    for i in zigzag_indices:
        _1d_array[1] = block[zigzag_indices[0], zigzag_indices[1]]

    return _1d_array