import numpy as np


def run_length_decoder(encoded):
    encoded_len = encoded.shape
    image = np.array([])
    for i in range(encoded_len[0]):
        if encoded[i-1] == 0:
            continue
        if encoded[i] == 0:
            zeros = np.zeros(encoded[i+1])
            image = np.append(image,zeros)
        else:
            image = np.append(image,encoded[i])
    return image

print(run_length_decoder(np.array([1, 2, 3, 0, 4, 1, 0, 1, 1, 9, 0, 2, 9])))
