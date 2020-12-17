import cv2
from os import listdir
import os.pathhh
import cli
import sys
from init_file import get_settings
from filters.grayscal import make_it_gray
from filters.blur import blur
from filters.dilate import dilate

# Variable initiation
path = '/Users/Ugo/Documents/dev/itescia/08_imageFilter/python-imagefilter-team-9/'
#path = 'C:/Users/DOBRO/Desktop/Filter/'

commands = cli.check_args()

# Change input directory, output directory, log file and init file if user wants it
for k, v in commands.items():
    if k == 'logger_file':
        logger_file = v
    elif k == 'input_dir':
        input_dir = v
    elif k == 'output_dir':
        output_dir = v
    elif k == 'init_file':
        init_file = v


# Check if input directory doesn't exists
if not os.path.exists(input_dir):
    os.mkdir(input_dir)

# Check if output directory doesn't exists
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Check if user given filters parameters
try :
    filters = commands['filters']
except KeyError:
    print('No filters given')
    sys.exit()


imgs = listdir(path + input_dir)

for img in imgs:
    img_extension = os.path.splitext(path + input_dir + img)[1]

    # Check if file is an image
    if img_extension == '.png' or img_extension == '.jpg':

        # Read image
        image = cv2.imread(f'{path}{input_dir}/{img}')

        # Apply filters
        for k, v in filters.items():
            if k == 'blur':
                image = blur(image, int(v))

            if k == 'dilate':
                image = dilate(image, int(v))

            if k == 'grayscal':
                image = make_it_gray(image)

        # Save the new image
        cv2.imwrite(f'{path}{output_dir}/{img}', image)

print('Done !')
