from datetime import datetime
log_file = 'image_filter.log'

    # create the log file format
def log(msg):
    now = datetime.now()
    timestamp = now.strftime('%d/%m/%Y %H:%M:%S')
    formatted = f'{timestamp} - {msg}'
    with open(log_file, 'a') as f:
        f.write(formatted + '\n')