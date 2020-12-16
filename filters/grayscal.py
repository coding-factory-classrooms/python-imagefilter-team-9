import cv2

def make_it_gray():
    racine = '/Users/Ugo/Documents/dev/itescia/08_imageFilter/python-imagefilter-team-9/'
    #racine = 'C:\Users\DOBRO\Desktop\Filter\img\'

    image = cv2.imread(f'{racine}img/img1.jpg')
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'{racine}out/img1.jpg', image_gray)