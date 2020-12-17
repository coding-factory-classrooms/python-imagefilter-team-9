from datetime import datetime


# create the log file format
def log(msg, log_file):
    """
    Print in the console and write in the log file a specific message
    :param msg: message to print in the console and write in the log file
    :param log_file: file where the function writes the message
    """
    now = datetime.now()
    timestamp = now.strftime('%d/%m/%Y %H:%M:%S')
    formatted = f'{timestamp} - {msg}'
    print(formatted)

    with open(log_file, 'a') as f:
        f.write(formatted + '\n')