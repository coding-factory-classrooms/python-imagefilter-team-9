import cv2
from os import listdir
import os.path
import cli
from filters.grayscal import make_it_gray
from filters.blur import blur
from filters.dilate import dilate

# Variable initiation
path = '/Users/Ugo/Documents/dev/itescia/08_imageFilter/python-imagefilter-team-9/'
#path = 'C:/Users/DOBRO/Desktop/Filter/'

input_dir = 'img'
output_dir = 'out'
logger_file = 'image_filter.log'
command_dictionary = cli.check_args()

# Change input directory, output directory and log file if user
for k, v in command_dictionary.items():
    if k == 'logger_file':
        logger_file = v
    elif k == 'input_directory':
        input_dir = v
    elif k == 'output_directory':
        output_dir = v

# Check if input directory doesn't exists
if not os.path.exists(input_dir):
    os.mkdir(input_dir)

# Check if output directory doesn't exists
if not os.path.exists(output_dir):
    os.mkdir(output_dir)


imgs = listdir(path + input_dir)
filters = command_dictionary['filters']

for img in imgs:
    img_extension = os.path.splitext(path + input_dir + img)[1]

    # Check if file is an image
    if img_extension == '.png' or img_extension == '.jpg':

        # Read image
        image = cv2.imread(f'{path}{input_dir}/{img}')

        # Apply filters and save the new image
        for k, v in filters.items():
            if k == 'blur':
                image = blur(image, int(v))
                print(f'{img} was blured')

            if k == 'dilate':
                image = dilate(image, int(v))
                print(f'{img} was dilated')

            if k == 'grayscale':
                image = make_it_gray(image)
                print(f'{img} was grayscaled')

        cv2.imwrite(f'{path}{output_dir}/{img}', image)

# blur(image, 9)
# dilate(image, 10)



