import random
import time
from datetime import datetime, timedelta
import os

def simulate_live_entries(file_path, duration_seconds=60, interval=1, timezone_offset=2):
    # Open the file in binary mode to perform the end-relative seek
    with open(file_path, 'rb+') as f:
        f.seek(0, 2)  # Move to the end of the file
        # If the file is non-empty and does not end with a newline, add one
        if f.tell() > 0:  # Check if the file is not empty
            f.seek(-1, 2)  # Go to the last byte of the file
            if f.read(1) != b'\n':  # If the last byte is not a newline
                f.write(b'\n')  # Write a newline
    
    # Get hostnames from existing lines
    with open(file_path, 'r') as f:
        hostnames = set()
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 3:
                # This will add both the source and destination hostnames
                hostnames.update(parts[1:])

    # Convert your set to a list here
    hostname_list = list(hostnames)

    # Simulate live entry appending
    end_time = time.time() + duration_seconds
    while time.time() < end_time:
        current_time = datetime.utcnow() + timedelta(hours=timezone_offset)
        timestamp = int(current_time.timestamp() * 1000)  # Convert to milliseconds
        source = random.choice(hostname_list)  # Use the list here
        destination = random.choice(hostname_list)  # And here
            
        # Append a new log entry in text mode
        with open(file_path, 'a') as f:
            f.write(f"{timestamp} {source} {destination}\n")

        time.sleep(interval)

# Replace with the actual path to your log file
simulate_live_entries(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'input-file-10000.txt'))
