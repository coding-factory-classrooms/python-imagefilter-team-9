import cv2

def blur():
    racine = '/Users/Ugo/Documents/dev/itescia/08_imageFilter/python-imagefilter-team-9/'
    #racine = 'C:/Users/DOBRO/Desktop/Filter/'

    image_blur = cv2.GaussianBlur(image, (blur_intensity, blur_intensity), 0)
    return image_blur
