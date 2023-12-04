import numpy as np
from Blockify.blockify_image import blockify_image
from DCT.DCT import DCT
from DCT.DCT_Basis import DCT_Basis
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
    dct_basis = np.zeros((N,N,N,N))

    for u in range(N):
        for v in range(N):
            dct_basis[u][v] = DCT_Basis(u,v,N)

    dct_blocks = np.zeros(blocks.shape)

    for i in range(no_vertical_blocks):
        for j in range(no_horizontal_blocks):
            dct_blocks[i][j] = DCT(blocks[i][j], dct_basis)

    # [3] apply quantization to each block
    quantized_blocks = np.zeros(dct_blocks.shape)
    
    for i in range(no_vertical_blocks):
        for j in range(no_horizontal_blocks):
            quantized_blocks[i][j] = quantize(dct_blocks[i][j], CompressionMode)
    
    # [4] apply zigzag transform (2D to 1D) to each block
    total_no_blocks = no_vertical_blocks * no_horizontal_blocks
    _1D_blocks = np.empty((total_no_blocks,N*N))
    idx = 0
    for i in range(no_vertical_blocks):
        for j in range(no_horizontal_blocks):
                block = quantized_blocks[i][j]
                _1D_blocks[idx] = zigzag_transform(quantized_blocks[i][j])
                idx += 1
    
    # [5] apply run-length encoding to each block
    run_length_encoded_blocks = np.array([])
    sz = 0
    for i in range(total_no_blocks):
            _1D_block = run_length_encoder(_1D_blocks[i])
            run_length_encoded_blocks = np.append(run_length_encoded_blocks, _1D_block)

    # [6] apply Entropy encoding to each block
    encoded_data, huffman_tree = huffman_encode(run_length_encoded_blocks)
    
    return encoded_data, huffman_tree, no_vertical_blocks, no_horizontal_blocks
