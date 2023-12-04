from Utilities.read_image import read_image
from DEFS import CompressionMode
from encoder import encoder
import numpy as np

def main():
    N = 8
    image_path = "./palestine.jpg"
    image_array, padding_length, padding_width = read_image(image_path, N)
    
    compression_mode = CompressionMode.HIGH
    encoded_data, huffman_tree = encoder(image_array, N, compression_mode)

    print(encoded_data)


if __name__ == "__main__":
    main()