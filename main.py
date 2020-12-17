import cv2
import cli
import sys
import logger
import os.path
from os import listdir
from filters.blur import blur
from filters.dilate import dilate
from filters.grayscal import make_it_gray
from filters.filter_ze_team import filter_ze_team
from init_file import get_default_input_dir, get_default_output_dir

# Variable initiation
logger_file = 'image_filter.log'
path = '/Users/Ugo/Documents/dev/itescia/08_imageFilter/python-imagefilter-team-9/'
#path = 'C:/Users/DOBRO/Desktop/Filter/'

# If user doesn't give input or output directory in CLI, get them from the init file
init_file = 'filterimg.ini'
input_dir = get_default_input_dir(init_file)
output_dir = get_default_output_dir(init_file)

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


logger.log(f'Program was run with parameters :\n{commands}', logger_file)
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
                logger.log(f'{img} was blurred with an intensity of {v}', logger_file)

            if k == 'dilate':
                image = dilate(image, int(v))
                logger.log(f'{img} was dilated with an intensity of {v}', logger_file)

            if k == 'grayscal':
                image = make_it_gray(image)
                logger.log(f'{img} was converted into black and white', logger_file)

            if k == 'filter_ze_team':
                image = filter_ze_team(image)
                logger.log(f'The names of the team was wrote on the image {img}', logger_file)

        # Save the new image
        cv2.imwrite(f'{path}{output_dir}/{img}', image)

logger.log('Done !', logger_file)
