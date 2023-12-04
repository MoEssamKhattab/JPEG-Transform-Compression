import numpy as np
from Blockify.blockify_image import blockify_image
from DCT.DCT import DCT
from Quantizer.quantize import quantize
from ZigzagTransform.zigzag_transform import zigzag_transform
from RunLength.Run_Length_Encoder import run_length_encoder
from HuffmanCode.huffman_encode import huffman_encode

def encoder(image_array, N, CompressionMode):

    # [1] blockify the image
    blocks = blockify_image(image_array, N)
    no_vertical_blocks = len(blocks)
    no_horizontal_blocks = len(blocks[0])
    
    # [2] apply DCT to each block
    dct_blocks = np.zeros(blocks.shape)
    
    for i in range(no_vertical_blocks):
        for j in range(no_horizontal_blocks):
            dct_blocks[i][j] = DCT(blocks[i][j])

    # [3] apply quantization to each block
    quantized_blocks = np.zeros(dct_blocks.shape)
    
    for i in range(no_vertical_blocks):
        for j in range(no_horizontal_blocks):
            quantized_blocks[i][j] = quantize(dct_blocks[i][j], CompressionMode)
    
    # [4] apply zigzag transform (2D to 1D) to each block
    total_no_blocks = no_vertical_blocks * no_horizontal_blocks
    _1D_blocks = np.array([])

    for i in range(no_vertical_blocks):
        for j in range (no_horizontal_blocks):
                _1D_blocks = np.append(_1D_blocks, zigzag_transform(quantized_blocks[i][j]))
    
    # [5] apply run-length encoding to each block
    run_length_encoded_blocks = np.array([])
    
    for i in range(len(_1D_blocks)):
        run_length_encoded_blocks = np.append(run_length_encoded_blocks, run_length_encoder(_1D_blocks(i)))

    # [6] apply Entropy encoding to each block
    run_length_encoded_blocks = run_length_encoded_blocks.reshape(1, -1).squeeze()
    encoded_data, huffman_tree = huffman_encode()
    
    return encoded_data, huffman_tree