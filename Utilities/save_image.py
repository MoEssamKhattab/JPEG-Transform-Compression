import matplotlib.pyplot as plt

def save_image(decoded_image, compression_mode):
    """
    Save the decoded image as jpg
    :param decoded_image: decoded image
    :return: None
    """
    plt.imsave(f'{"original_image" if compression_mode == None else compression_mode}.jpg', decoded_image, cmap='gray')