from DCT.DCT import DCT 
import numpy as np

if __name__ == "__main__":

    A = np.array([[231, 224, 224, 217, 217, 203, 189, 196],
                [210, 217, 203, 189, 203, 224, 217, 224],
                [196, 217, 210, 224, 203, 203, 196, 189],
                [210, 203, 196, 203, 182, 203, 182, 189],
                [203, 224, 203, 217, 196, 175, 154, 140],
                [182, 189, 168, 161, 154, 126, 119, 112],
                [175, 154, 126, 105, 140, 105, 119,  84],
                [154,  98, 105,  98, 105,  63, 112,  84]])

    C = DCT(A)

    print(C)