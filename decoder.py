import numpy as np
from HuffmanCode.huffman_decode import huffman_decode
from ZigzagTransform.reverse_zigzag_transform import reverse_zigzag_transform
from RunLength.Run_Length_Decocder import run_length_decoder
from Quantizer.dequantize import dequantize
from DCT.IDCT import IDCT
from DCT.IDCT_Basis import IDCT_Basis
from Blockify.deblockify_image import deblockify_image

def decoder(encoded_image,N,CompressionMode, HoriziontalPadding, VerticalPadding, HuffmanTree, no_vertical_blocks,no_horizontal_blocks):

    # [1] apply Entropy decoding to encoded image
    entropy_decoded_image = np.array(huffman_decode(encoded_image,HuffmanTree))
    
    # [2] apply run-length decoding
    runlength_decoded_image = run_length_decoder(entropy_decoded_image, no_vertical_blocks, no_horizontal_blocks, N)
    
    # [3] apply reverse zigzag transform (1D to 2D)
    
    blocks = np.zeros((no_vertical_blocks, no_horizontal_blocks ,N,N))
    
    runlength_decoded_size = runlength_decoded_image.shape[0]

    # image_total_pixels = no_vertical_blocks*no_horizontal_blocks*N*N

    index = 0
    for i in range(no_vertical_blocks):
        for j in range(no_horizontal_blocks):
            block = runlength_decoded_image[index:index+N*N]
            block = block.reshape((N, N))
            blocks[i][j] = block
            index += N*N

    # [4] apply dequantization to each block

    dequantized_blocks = np.zeros(blocks.shape)

    for i in range(no_vertical_blocks):
        for j in range(no_horizontal_blocks):
            dequantized_blocks[i][j] = dequantize(blocks[i][j], CompressionMode)

    # [5] apply IDCT to each block
    idct_basis = np.zeros((N,N,N,N))

    for x in range(N):
        for y in range(N):
            idct_basis[x][y] = IDCT_Basis(x,y,N)

    idct_blocks = np.zeros(blocks.shape)

    for i in range(no_vertical_blocks):
        for j in range(no_horizontal_blocks):
            idct_blocks[i][j] = IDCT(dequantized_blocks[i][j], idct_basis)

    # [6] deblockify the image
    return deblockify_image(idct_blocks)