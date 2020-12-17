import cv2

def filter_ze_team(image):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2

    image_with_ze_team = cv2.putText(image, 'Kevin, Enzo et Ugo', org, font, fontScale, color, thickness, cv2.LINE_AA)
    return image_with_ze_team