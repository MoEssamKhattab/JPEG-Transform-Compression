from DCT.DCT import DCT
from DCT.IDCT import IDCT
from read_image import read_image
import numpy as np

def main():
    N = 8
    image_array, padding_length, padding_width = read_image("./palestine.jpg", N)
    
    
    



if __name__ == "__main__":
    main()