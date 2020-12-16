import cv2
import numpy as np

def dilate():
    racine = '/Users/Ugo/Documents/dev/itescia/08_imageFilter/python-imagefilter-team-9/'
    # racine = 'C:/Users/DOBRO/Desktop/Filter/'

    kernel = np.ones((10, 10), np.uint8)

    image = cv2.imread(f'{racine}img/img1.jpg')
    image_dilate = cv2.dilate(image,kernel,iterations = 1)
    cv2.imwrite(f'{racine}out/img1.jpg', image_dilate)