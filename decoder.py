import numpy as np
from HuffmanCode.huffman_decode import huffman_decode
from ZigzagTransform.reverse_zigzag_transform import reverse_zigzag_transform
from RunLength.Run_Length_Decocder import run_length_decoder

def decoder(encoded_image,N,CompressionMode, HoriziontalPadding, VerticalPadding, HuffmanTree, no_vertical_blocks,no_horizontal_blocks):

    decoded_huffman_image = np.array(huffman_decode(encoded_image,HuffmanTree))
    decoded_runlength_image = run_length_decoder(decoded_huffman_image,no_vertical_blocks,no_horizontal_blocks,N)
    total_number_of_blocks = no_vertical_blocks*no_horizontal_blocks
    blocks = np.zeros((total_number_of_blocks,N,N))
    length_decoded_runlength = decoded_runlength_image.shape[0]
    



