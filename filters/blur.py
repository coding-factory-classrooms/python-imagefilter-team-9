import cv2

def blur(image, blur_intensity):
    """
    Apply blur effect on an image
    :param image: image on which we well apply the effect
    :param blur_intensity: the intensity of blur
    :return: the image blurred
    """
    image_blur = cv2.GaussianBlur(image, (blur_intensity, blur_intensity), 0)
    return image_blur
