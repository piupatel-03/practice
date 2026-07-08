#Log Writer: Write a log_message(level, message) function that appends timestamped entries to 
#a log.txt file. 

import datetime

def log_message(level, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - {level.upper()}: {message}\n")
#Example usage
log_message("info", "This is an informational message.")
log_message("warning", "This is a warning message.")
log_message("error", "This is an error message.")

