import cv2

def blur(image, blur_intensity):

    image_blur = cv2.GaussianBlur(image, (blur_intensity, blur_intensity), 0)
    return image_blur
