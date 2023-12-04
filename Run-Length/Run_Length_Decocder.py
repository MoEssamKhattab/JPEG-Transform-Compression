import numpy as np


def run_length_decoder(encoded):
    """
    Run-Length Decoder for binary image decompression.

    Parameters:
    - encoded (numpy.ndarray): Input array containing alternating counts of consecutive zeros and non-zero values.

    Returns:
    - image (numpy.ndarray): Decoded binary image represented as a NumPy array.

    Description:
    This function takes an encoded array, produced by a run-length encoder, and performs run-length decoding.
    """
    encoded_len = encoded.shape
    image = np.array([])
    for i in range(encoded_len[0]):
        if encoded[i - 1] == 0:
            continue
        if encoded[i] == 0:
            zeros = np.zeros(int(encoded[i + 1]))
            image = np.append(image, zeros)
        else:
            image = np.append(image, encoded[i])
    return image
