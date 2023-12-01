def image_to_blocks(image_array, N):
    """
    Divide an image array into blocks of size (N*N).
    :param image_array: numpy array of image
    :param N: size of blocks (N*N)
    :return: list of blocks
    """
    img_lenght, img_width = image_array.shape

    blocks = []
    for i in range(0, img_lenght, N):
        for j in range(0, img_width, N):
            blocks.append(image_array[i:i + N, j:j + N])
    return blocks