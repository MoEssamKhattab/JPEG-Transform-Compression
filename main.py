from Utilities.read_image import read_image
from DEFS import CompressionMode
from encoder import encoder
import numpy as np
from Utilities.calculate_compression_ratio import calculate_comprrssion_ratio
from decoder import decoder
from Utilities.save_image import save_image
import matplotlib.pyplot as plt

def main():

    # ==================== Read Image =======================
    N = 8
    image_path = "./palestine.jpg"
    image_array, vertical_padding, horizontal_padding = read_image(image_path, N)

    # ==================== Encode Image =======================
    compression_mode = CompressionMode.LOW
    encoded_data, huffman_tree, no_vertical_blocks ,no_horizontal_blocks = encoder(image_array, N, compression_mode)

    # ==================== Decode Image =======================
    decoded_image = decoder(encoded_data, N, compression_mode, vertical_padding, horizontal_padding, huffman_tree,no_vertical_blocks,no_horizontal_blocks)

    # ==================== Calculate Compression Ratio =======================
    compression_ratio = calculate_comprrssion_ratio(image_array,encoded_data)
    print(f"Compression ratio: {compression_ratio}:1")

    # ==================== Show and Save Image =======================
    # save the decoded image as jpg
    
    original_image = image_array[:decoded_image.shape[0] - vertical_padding, :decoded_image.shape[1] - horizontal_padding]
    save_image(original_image, decoded_image, compression_ratio, compression_mode)


if __name__ == "__main__":
    main()