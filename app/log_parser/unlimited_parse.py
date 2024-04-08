import sched
import time
from collections import Counter
from .parse_data import HostsConnectedTo
from datetime import datetime, timedelta
import pytz

REPEAT_EVERY = 3600  # Schedule the task to run every hour as requested in the assignment

class UnlimitedParser:
    """
    Continuously parses a log file to find host connection details within the last hour.
    Outputs the following every hour:
    - A list of hostnames connected to a specified host
    - A list of hostnames that received connections from the specified host
    - The hostname that generated the most connections in the last hour
    """

    def __init__(self, file, host=None):
        self.file = file
        self.host = host
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def process_entries(self, init_datetime, end_datetime, received):
        parser = HostsConnectedTo(self.file, init_datetime, end_datetime, hostname=self.host, received=received)
        entries = list(parser.parse_file())  # This ensure a list is always created, even if it's empty.
        return set(entries)

    def hostname_most_connections_hour(self, init_datetime, end_datetime):
        """
        Finds the hostname that has the most connections in the last hour.

        Args:
            init_datetime (int): The start time as Unix timestamp.
            end_datetime (int): The end time as Unix timestamp.

        Returns:
            list: A list of tuples with the hostnames that have the most connections and their counts.
        """
        parser = HostsConnectedTo(self.file, init_datetime, end_datetime)
        all_hostnames = list(parser.parse_file_for_most_connections())

        if not all_hostnames:
            return []

        counter = Counter(all_hostnames)
        max_count = max(counter.values(), default=0)
        most_common_hostnames = [(hostname, count) for hostname, count in counter.items() if count == max_count]

        return most_common_hostnames
    
    def unlimited_parse(self, sc):
        """
        Schedules the parser to run every hour and prints the connection details.
        """
        # Get the current time and timestamps for the last hour
        gmt_plus_2 = pytz.timezone('Etc/GMT+2')

        # Get the current time in GMT+2 and calculate timestamps for the last hour in milliseconds
        current_time = datetime.now(tz=gmt_plus_2)
        one_hour_ago = current_time - timedelta(hours=1)
        
        one_hour_ago_timestamp = int(one_hour_ago.timestamp()) * 1000  # Corrected to milliseconds
        current_timestamp = int(current_time.timestamp()) * 1000  # Corrected to milliseconds
        
        print(f"Debug: Checking from {one_hour_ago_timestamp} to {current_timestamp}")

        result_connected_to = self.process_entries(one_hour_ago_timestamp, current_timestamp, False)
        result_received_from = self.process_entries(one_hour_ago_timestamp, current_timestamp, True)
        result_most_connections = self.hostname_most_connections_hour(one_hour_ago_timestamp, current_timestamp)

        print(f"\nHostnames connected to {self.host} in the last hour: {', '.join(result_connected_to) if result_connected_to else 'None'}")
        print(f"Hostnames received connections from {self.host} in the last hour: {', '.join(result_received_from) if result_received_from else 'None'}")
        print(f"The hostname(s) that generated most connections in the last hour: {', '.join(f'{host} ({count})' for host, count in result_most_connections) if result_most_connections else 'None'}")
        print(f"Waiting {REPEAT_EVERY} seconds for the next check...")
        
        sc.enter(REPEAT_EVERY, 1, self.unlimited_parse, (sc,))

    def run(self):
        """
        Starts the scheduler to run the parser every hour.
        """
        self.scheduler.enter(0, 1, self.unlimited_parse, (self.scheduler,))
        self.scheduler.run()
