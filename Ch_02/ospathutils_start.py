# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # Print the name of the OS
    print("Operating System:", os.name)

    # Check for item existence and type
    file_path = "example.txt"
    if path.exists(file_path):
        print(f"{file_path} exists.")
        if path.isfile(file_path):
            print(f"{file_path} is a file.")
        elif path.isdir(file_path):
            print(f"{file_path} is a directory.")
    else:
        print(f"{file_path} does not exist.")

    # Work with file paths
    dir_path = path.dirname(file_path)
    print(f"Directory part of the file path: {dir_path}")
    base_name = path.basename(file_path)
    print(f"Base name of the file path: {base_name}")

    # Get the modification time
    if path.exists(file_path):
        mod_time = path.getmtime(file_path)
        print(f"Last modified time of {file_path}: {mod_time}")
        # Convert to a human-readable format
        print("Formatted modification time:", time.ctime(mod_time))

    # Calculate how long ago the item was modified
    if path.exists(file_path):
        mod_time = path.getmtime(file_path)
        current_time = time.time()  # Get the current time in seconds since the epoch
        time_diff = current_time - mod_time  # Difference in seconds
        print(f"Time difference in seconds: {time_diff}")
        # Convert seconds to days, hours, minutes, and seconds
        days = time_diff // (24 * 3600)
        time_diff = time_diff % (24 * 3600)
        hours = time_diff // 3600
        time_diff %= 3600
        minutes = time_diff // 60
        seconds = time_diff % 60
        print(f"Time since last modification: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds.")

if __name__ == "__main__":
    main()
