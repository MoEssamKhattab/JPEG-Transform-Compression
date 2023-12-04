from Utilities.read_image import read_image
from DEFS import CompressionMode
from encoder import encoder
import numpy as np
from Utilities.calculate_compression_ratio import calculate_comprrssion_ratio
from decoder import decoder

def main():
    N = 8
    image_path = "./palestine.jpg"
    image_array, padding_length, padding_width = read_image(image_path, N)
    
    compression_mode = CompressionMode.LOW
    encoded_data, huffman_tree, no_vertical_blocks ,no_horizontal_blocks = encoder(image_array, N, compression_mode)

   # print(encoded_data)

    decoded_image = decoder(encoded_data,N,compression_mode,padding_length,padding_width,huffman_tree,no_vertical_blocks,no_horizontal_blocks)

    print(np.min(decoded_image))

    compression_ratio = calculate_comprrssion_ratio(image_array,encoded_data)
    print(compression_ratio)
    
    import matplotlib.pyplot as plt

    plt.imshow(decoded_image, cmap='gray')
    plt.show()







if __name__ == "__main__":
    main()