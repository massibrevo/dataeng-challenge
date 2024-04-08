import unittest
import os
import sys

# Setting here the system path to include the parent directory, allowing for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.log_parser.parse_data import HostsConnectedTo

class TestParseData(unittest.TestCase):
    """
    Test suite for the HostsConnectedTo class.

    The tests cover multiple scenarios ensuring that the log parsing
    functionality works as expected, returning the correct hosts
    connected within a specified time range.
    """
    
    @classmethod
    def setUpClass(self):
        """
        Class method called before tests in an individual class are run.
        """
        # Test file path relative to the test module.
        self.test_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'input-file-10000.txt')
        self.init_datetime = 1565732487029  # This is the timestamp of the first entry to check in the data (can be adjusted)
        self.end_datetime = 1565732493074  # This is the timestamp of the second entry to check in the data (can be adjusted)

    def test_hosts_connected_to_within_range(self):
        """
        Test if the parser returns the correct connections for a given host within the time range.
        """
        # Arrange
        hostname = 'Klohe' # Selecting one hostname for the test
        expected_results = ['Joaneliz']

        # Act
        parser = HostsConnectedTo(self.test_file_path, self.init_datetime, self.end_datetime, hostname=hostname, received=True)
        results = list(parser.parse_file())

        self.assertEqual(results, expected_results)

    def test_no_hosts_connected_outside_range(self):
        """
        Test if the parser returns an empty list when querying outside the range of the data.
        """
        # Arrange
        
        hostname = 'NonExistentHost'
        expected_results = []  # No connections expected

        parser = HostsConnectedTo(self.test_file_path, self.init_datetime, self.end_datetime, hostname=hostname)
        results = list(parser.parse_file())

        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()
