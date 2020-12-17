import cv2

def make_it_gray(image):
    """
    Apply grayscale effect on an image
    :param image: image on which we well apply the effect
    :return: the image in black and white
    """
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image_gray