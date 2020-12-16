import cv2

def dilate():
    racine = '/Users/Ugo/Documents/dev/itescia/08_imageFilter/python-imagefilter-team-9/'
    # racine = 'C:\Users\DOBRO\Desktop\Filter\imgs\MV.png'

    image = cv2.imread(f'{racine}img/img1.jpg')
    image_dilate = cv2.dilate(image, )
    cv2.imwrite(f'{racine}out/img1.jpg', image_dilate)