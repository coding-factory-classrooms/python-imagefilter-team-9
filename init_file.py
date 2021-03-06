from configparser import SafeConfigParser

def get_settings(init_file):
    """
    Get all data from init file
    :param init_file: path of the init file
    :return: a dictionary with input dir, output dir, log file and filters
    """
    # Variables initiation
    init_var_dictionary = {}
    filter_dictionary = {}

    # Use configParser to get data from the init file
    parser = SafeConfigParser()
    parser.read(init_file)

    init_var_dictionary['input_dir'] = parser.get('general', 'input_dir')
    init_var_dictionary['output_dir'] = parser.get('general', 'output_dir')
    init_var_dictionary['log_file'] = parser.get('general', 'log_file')

    filters_array = parser.get('filters', 'content').split('|')

    # Get all filters in the init file
    for filter in filters_array:
        filters_value = filter.split(':')

        try:
            filter_dictionary[filters_value[0]] = filters_value[1]
        except IndexError:
            filter_dictionary[filters_value[0]] = ''

    # Push all filters in the filter_dictionary
    init_var_dictionary['filters'] = filter_dictionary

    return init_var_dictionary

def get_default_input_dir(init_file):
    """
    Get the input directory from the default init file
    :param init_file: path of the init file
    :return: path of the default input file
    """
    parser = SafeConfigParser()
    parser.read(init_file)
    input_dir = parser.get('general', 'input_dir')

    return input_dir


def get_default_output_dir(init_file):
    """
    Get the output directory from the default init file
    :param init_file: path of the init file
    :return: path of the default output file
    """
    parser = SafeConfigParser()
    parser.read(init_file)
    output_dir = parser.get('general', 'output_dir')

    return output_dir




