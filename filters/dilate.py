import cv2
import numpy as np

def dilate(image, dilate_intensity):

    x =0
    kernel = np.ones((dilate_intensity, dilate_intensity), np.uint8)
    image_dilate = cv2.dilate(image, kernel, iterations = 1)
    return image_dilate
