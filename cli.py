import os
import sys
from os import listdir

import init_file
import logger
import inspect
import filters as filters

args = sys.argv

def check_args():
    """
    Get args given by the user in the CLI
    :return: a dictionary with all the commands given by the user
    """
    filter_dictionary = {}
    command_dictionary = {}

    # Check if there is args
    if len(args) > 1:
        if args[1] == '-h':
            print('Usage : imagefilter')
            print('-h, ----help')
            print('-i, --input-dir <directory>')
            print('-o, --output-dir <directory>')
            sys.exit()

        else:
            i = 1
            while i < len(args):
                # Detect an argument
                if args[i][0] == '-':
                    try:
                        # Check if there is some parameters after '--filters' argument
                        if args[i] == '--filters' and args[i+1]:
                            filters_array = args[i+1].split('|')
                            for x in filters_array:
                                filter_value = x.split(':')

                                try:
                                    if filter_value[0] == 'blur' and int(filter_value[1]) % 2 != 0 or filter_value[0] == 'dilate' and int(filter_value[1]) % 2 != 0 or filter_value[0] == 'grayscal' or filter_value[0] == 'filter_ze_team':
                                        try:
                                            filter_dictionary[filter_value[0]] = filter_value[1]
                                        except IndexError:
                                            filter_dictionary[filter_value[0]] = ''

                                    else:
                                        print('Invalid filters command')
                                        sys.exit()

                                except ValueError:
                                    print('Invalid number given to filter value')
                                    sys.exit()

                            # Give to command_dictionary all filters data
                            command_dictionary['filters'] = filter_dictionary

                        # Check if there is a parameter after '-i' argument
                        elif args[i] == '-i' and len(args) >= i+1:
                            input_directory = args[i+1]
                            command_dictionary['input_dir'] = input_directory

                        # Check if there is a parameter after '-o' argument
                        elif args[i] == '-o' and len(args) >= i+1:
                            output_directory = args[i+1]
                            command_dictionary['output_dir'] = output_directory

                        # Check if there is a parameter after '--log-file' argument
                        elif args[i] == '--log-file' and len(args) >= i+1:
                            logger_file = args[i+1]
                            command_dictionary['logger_file'] = logger_file

                        # Check if there is a parameter after '--config-file' argument
                        elif args[i] == '--config-file' and len(args) >= i+1:
                            filterimg = args[i+1]
                            command_dictionary['init_file'] = filterimg

                        # Check if there is a parameter after '--config-file' argument
                        elif args[i] == '--list-filters' and len(args) >= i+1:
                            filters_package = listdir('filters')

                            print('Available filters :')
                            for filter_file in filters_package:
                                file_extension = os.path.splitext(filter_file)[1]
                                if file_extension == '.py':
                                    print(' - ' + filter_file.replace('.py', ''))
                            sys.exit()

                        else:
                            print(f'{args[i]} is an invalid command')
                            sys.exit()
                    except IndexError:
                        print('Invalid command')
                        sys.exit()

                i += 1
    # Case where there is no arg, then take data from init file
    else:
        init_file_path = 'filterimg.ini'
        command_dictionary = init_file.get_settings(init_file_path)

    logger.log(f'Program was run with parameters :\n{command_dictionary}')
    return command_dictionary

