import cv2

def blur():
    racine = '/Users/Ugo/Documents/dev/itescia/08_imageFilter/python-imagefilter-team-9/'
    #racine = 'C:/Users/DOBRO/Desktop/Filter/'

    blur_intensity = 33

    image = cv2.imread(f'{racine}img/img1.jpg')
    image_blur = cv2.GaussianBlur(image, (blur_intensity, blur_intensity), 0)
    cv2.imwrite(f'{racine}out/img1.jpg', image_blur)