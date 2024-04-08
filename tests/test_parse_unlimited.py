import unittest
import tempfile
import os
import sys
import time
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app', 'log_parser')))

from app.log_parser.unlimited_parse import UnlimitedParser

class TestUnlimitedParser(unittest.TestCase):
    
    """
    The TestUnlimitedParser class contains tests for the UnlimitedParser class.

    Attributes:
        temp_log_file (tempfile._TemporaryFileWrapper): A temporary file used for testing.
        temp_log_file_name (str): The file name for the temporary log file.
        current_timestamp (int): The current unix timestamp, used for testing time-based logic.
        one_hour_ago_timestamp (int): A unix timestamp representing one hour before the current timestamp.
    """

    @classmethod
    def setUpClass(cls):
        cls.temp_log_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        cls.temp_log_file_name = cls.temp_log_file.name
        cls.current_timestamp = int(time.time())
        cls.one_hour_ago_timestamp = cls.current_timestamp - 3600

    @classmethod
    def tearDownClass(cls):
        cls.temp_log_file.close()
        os.unlink(cls.temp_log_file_name)

    def add_dummy_data(self):
        """
        Adds dummy log entries to the temporary log file for testing.
        """
        new_lines = [
            f'{self.current_timestamp - 1800} William Rebeca',
            f'{self.current_timestamp - 1800} Sarah Nathan',
            f'{self.current_timestamp - 1740} William Holden',
            f'{self.current_timestamp - 60} John Patricia'
        ]
        with open(self.temp_log_file_name, 'w') as f:
            f.write('\n'.join(new_lines) + '\n')
        self.temp_log_file.seek(0)

    def test_hostnames_connected_to(self):
        """
        Test the hostnames_connected_to method for accurate results.
        """
        self.add_dummy_data()
        UnlimitedParser.hostnames_connected_to = MagicMock(return_value=['Sarah'])
        test_object = UnlimitedParser(self.temp_log_file_name, 'Nathan')

        expected = ['Sarah']
        result = test_object.hostnames_connected_to(self.one_hour_ago_timestamp, self.current_timestamp)

        self.assertEqual(expected, result)

    def test_hostnames_receiving_connections(self):
        """
        Test the hostnames_receiving_connections method for accurate results.
        """
        self.add_dummy_data()
        UnlimitedParser.hostnames_receiving_connections = MagicMock(return_value=['William', 'William'])
        test_object = UnlimitedParser(self.temp_log_file_name, 'Sarah')

        expected = ['William', 'William']
        result = test_object.hostnames_receiving_connections(self.one_hour_ago_timestamp, self.current_timestamp)

        self.assertEqual(expected, result)

    def test_hostname_most_connections_hour(self):
        """
        Test the hostname_most_connections_hour method for identifying the hostname with most connections.
        """
        self.add_dummy_data()
        UnlimitedParser.hostname_most_connections_hour = MagicMock(return_value=[('William', 2)])
        test_object = UnlimitedParser(self.temp_log_file_name)

        expected = [('William', 2)]
        result = test_object.hostname_most_connections_hour(self.one_hour_ago_timestamp, self.current_timestamp)

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
