from datetime import datetime


# create the log file format
def log(msg, log_file):
    now = datetime.now()
    timestamp = now.strftime('%d/%m/%Y %H:%M:%S')
    formatted = f'{timestamp} - {msg}'
    print(formatted)

    with open(log_file, 'a') as f:
        f.write(formatted + '\n')