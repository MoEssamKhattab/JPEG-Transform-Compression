import numpy as np


def run_length_encoder(image):
    zeroscount = 0
    len = image.shape
    encoded = np.array([])
    for i in range(len[0]):
        if image[i] == 0:
            if zeroscount == 0:
                encoded = np.append(encoded,0)
            zeroscount += 1
        else:
            if zeroscount != 0:
                encoded = np.append(encoded, zeroscount)
                zeroscount = 0
            encoded = np.append(encoded,image[i])
    return encoded

print(run_length_encoder(np.array([1,2,3,0,0,0,0,1,0,1,9,0,0,9])))