import os



class HostsConnectedTo:
    """
    Parses the data within a specified time range.
    Given a filename with the specified format, an init_datetime, and an end_datetime,
    returns a list of hostnames connected to or from a given host during the specified period.
    
    Parameters:
        file (str): The path to the log file.
        init_datetime (int): The start time as a Unix timestamp.
        end_datetime (int): The end time as a Unix timestamp.
        hostname (str): The hostname to search for connections. Default is None.
        received (bool): If True, finds hosts that received connections from 'hostname'.
                         If False, finds hosts that 'hostname' connected to. Default is False.
    """

    def __init__(self, file, init_datetime, end_datetime, hostname=None, received=False):
        self.file = file
        self.init_datetime = init_datetime
        self.end_datetime = end_datetime
        self.hostname = hostname
        self.received = received

    def parse_file(self):
        """
        Generator function that parses the log file and yields entries matching the specified criteria.
        
        Yields:
            list: Parts of the log line that match the criteria.
        """
        with open(self.file) as f:
            for line in f:
                parts = line.strip().split()
                timestamp = int(parts[0])
                
                if self.init_datetime <= timestamp <= self.end_datetime:
                    source_host, destination_host = parts[1], parts[2]
                    
                    # Only proceed if self.hostname is not None
                    if self.hostname:
                        source_host, destination_host = source_host.strip(), destination_host.strip()
                        if self.received and self.hostname.lower() == destination_host.lower():
                            yield source_host
                        elif not self.received and self.hostname.lower() == source_host.lower():
                            yield destination_host

    def parse_file_for_most_connections(self):
        """Yield all hostnames for the purpose of counting connections."""
        with open(self.file) as f:
            for line in f:
                parts = line.strip().split()
                timestamp = int(parts[0])
                
                if self.init_datetime <= timestamp <= self.end_datetime:
                    yield parts[1]  # Source hostname
                    yield parts[2]  # Destination hostname
                    
    # If no lines are yielded by this point, yield an empty list to ensure the return value is always iterable.
        yield from []

    def run(self):
        """
        Runs the parser, processes the log file, and prints out the results.
        """
        parsed_result = list(self.parse_file())
        # Check the direction of connection based on the 'received' flag
        if self.received:
            # When looking for received connections, the self.hostname should be at index 2 (right side)
            connected_hosts = set(hostname for hostname in parsed_result)
        else:
            # When looking for made connections, the self.hostname should be at index 1 (left side)
            connected_hosts = set(hostname for hostname in parsed_result)

        if connected_hosts:
            hosts_list = ', '.join(connected_hosts)
            print(f'Hosts connected to {self.hostname} from {self.init_datetime} to {self.end_datetime}: {hosts_list}')
        else:
            print(f'No hosts were connected to {self.hostname} from {self.init_datetime} to {self.end_datetime}')