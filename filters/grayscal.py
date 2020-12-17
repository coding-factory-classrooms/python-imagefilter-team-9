import cv2

def make_it_gray(image):

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image_gray