import cv2


def filter_ze_team(image):
    """
    Write the names of the team on an image
    :param image: image on which we will apply the effect
    :return: the image with the names of the team
    """
    font = cv2.FONT_HERSHEY_TRIPLEX
    org = (50, 50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2

    image_with_ze_team = cv2.putText(image, 'Kevin, Enzo et Ugo', org, font, fontScale, color, thickness, cv2.LINE_AA)
    return image_with_ze_team