import cv2
import numpy as np

def dilate(image, dilate_intensity):
    """
    Apply dilation effect on an image
    :param image: image on which we well apply the effect
    :param dilate_intensity: the intensity of dilation
    :return: the image dilated
    """
    kernel = np.ones((dilate_intensity, dilate_intensity), np.uint8)
    image_dilate = cv2.dilate(image, kernel, iterations = 1)
    return image_dilate
