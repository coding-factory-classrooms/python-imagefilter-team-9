import cv2
from filters.grayscal import make_it_gray
from filters.blur import blur
from filters.dilate import dilate
import cli


# make_it_gray()
# blur()
dilate()

args = cli.check_args()
print(args)