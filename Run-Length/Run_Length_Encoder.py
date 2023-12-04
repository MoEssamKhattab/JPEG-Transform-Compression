import numpy as np


def run_length_encoder(image):
    """
    Run-Length Encoder for binary image compression.

    Parameters:
    - image (numpy.ndarray): Input binary image represented as a NumPy array.

    Returns:
    - numpy.ndarray: Encoded array containing alternating counts of consecutive zeros and non-zero values.

    Description:
    This function takes a binary image represented as a NumPy array and performs run-length encoding on it.
    """
    zeros_count = 0
    length = image.shape
    encoded = np.array([])
    for i in range(length[0]):
        if image[i] == 0:
            if zeros_count == 0:
                encoded = np.append(encoded, 0)
            zeros_count += 1
        else:
            if zeros_count != 0:
                encoded = np.append(encoded, zeros_count)
                zeros_count = 0
            encoded = np.append(encoded, image[i])
    return encoded
