import numpy as np


def run_length_decoder(encoded,no_vertical_blocks,no_horizontal_blocks,N):
    """
    Run-Length Decoder for binary image decompression.

    Parameters:
    - encoded (numpy.ndarray): Input array containing alternating counts of consecutive zeros and non-zero values.

    Returns:
    - image (numpy.ndarray): Decoded binary image represented as a NumPy array.

    Description:
    This function takes an encoded array, produced by a run-length encoder, and performs run-length decoding.
    """
    total_image_length = N*N*no_horizontal_blocks*no_vertical_blocks

    encoded_len = encoded.shape
    image = np.zeros(total_image_length)
    idx = 0
    for i in range(encoded_len[0]):
        if encoded[i - 1] == 0:
            continue
        if encoded[i] == 0:
            for j in range(int(encoded[i+1])):
                image[idx] = 0
                idx += 1
        else:
            image[idx] = encoded[i]
            idx += 1
    return image
