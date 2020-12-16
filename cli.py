import sys

args = sys.argv

def check_args():

    filter_dictionary = {}

    if len(args) > 1:
        if args[1] == '-h':
            print('Usage : imagefilter')
            print('-h, ----help')
            print('-i, --input-dir <directory>')
            print('-o, --output-dir <directory>')

        else:
            i = 1
            while i < len(args):
                # Detect an argument
                if args[i][0] == '-':

                    if args[i] == '--filters' and args[i+1]:
                        filters_array = args[i+1].split('|')
                        for x in filters_array:
                            filter_value = x.split(':')

                            if filter_value[0] == 'blur' and int(filter_value[1]) or filter_value[0] == 'dilate' and int(filter_value[1]) or filter_value[0] == 'grayscale':
                                try:
                                    filter_dictionary[filter_value[0]] = filter_value[1]
                                except IndexError:
                                    filter_dictionary[filter_value[0]] = ''
                            else:
                                print('Invalid filters command')

                    elif args[i] == '-i' and len(args) >= i+1:
                        input_directory = args[i+1]
                        print('Input directory : ' + input_directory)

                    elif args[i] == '-o' and len(args) >= i+1:
                        output_directory = args[i+1]
                        print('Output directory : ' + output_directory)

                    else:
                        print(f'{args[i]} is an invalid command')




                i += 1
            print(filter_dictionary)

