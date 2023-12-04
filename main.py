from Utilities.read_image import read_image
from DEFS import CompressionMode
from encoder import encoder
import numpy as np
from Utilities.calculate_compression_ratio import calculate_comprrssion_ratio
from decoder import decoder
from PIL import Image

def main():

    # ==================== Read Image =======================
    N = 8
    image_path = "./Mona_Lisa.jpg"
    image_array, padding_length, padding_width = read_image(image_path, N)

    print(image_array.shape)
    # ==================== Encode Image =======================
    compression_mode = CompressionMode.LOW
    encoded_data, huffman_tree, no_vertical_blocks ,no_horizontal_blocks = encoder(image_array, N, compression_mode)

    # ==================== Decode Image =======================
    decoded_image = decoder(encoded_data,N,compression_mode,padding_length,padding_width,huffman_tree,no_vertical_blocks,no_horizontal_blocks)

    # ==================== Calculate Compression Ratio =======================
    compression_ratio = calculate_comprrssion_ratio(image_array,encoded_data)
    print(compression_ratio)

    # ==================== Restore Image =======================
    # restore image to original size and save it as jpg

    decoded_image = decoded_image[:decoded_image.shape[0] - padding_length, :decoded_image.shape[1] - padding_width]
    #decoded_image = decoded_image.astype(np.uint8)
    
    print(np.max(decoded_image))
    print(np.min(decoded_image))

    import matplotlib.pyplot as plt

    plt.imshow(decoded_image, cmap='gray')
    plt.show()

if __name__ == "__main__":
    main()