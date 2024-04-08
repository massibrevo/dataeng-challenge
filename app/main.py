import os
from datetime import datetime, timedelta
import pytz
from log_parser.parse_data import HostsConnectedTo
from log_parser.unlimited_parse import UnlimitedParser

FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'input-file-10000.txt')

class Menu:
    def __init__(self):
        self.init_datetime = None
        self.end_datetime = None
        self.hostname = None

    @staticmethod
    def get_option(options):
        print('\n'.join((f'{str(i)}. {name}' for i, name in options.items())))

        opt_input = input('Please, select an option: ')
        while not opt_input or not opt_input.isdigit() or opt_input.isspace() or int(opt_input) not in options.keys():
            opt_input = input('[Incorrect] Please, select an option: ')

        return int(opt_input)

    @staticmethod
    def get_timestamp(name):
        timestamp = input(f'[{name}]: ')
        while not timestamp or not timestamp.isdigit() or timestamp.isspace() or int(timestamp) < 1:
            timestamp = input(f'[{name}] incorrect: ')

        return int(timestamp)

    @staticmethod
    def get_username():
        hostname = input('[hostname]: ')
        while not hostname or hostname.isspace():
            hostname = input('[hostname] incorrect: ')

        return hostname

    def parse_data_init_end_time(self):
        print("### Parse the data with a time_init, time_end ###")
        self.init_datetime = self.get_timestamp('time_init')
        self.end_datetime = self.get_timestamp('time_end')
        self.hostname = self.get_username()
        
        try:
            parser = HostsConnectedTo(FILE, self.init_datetime, self.end_datetime, hostname=self.hostname)
            parser.run()
        except Exception as e:
            print(f'An error occurred: {str(e)}')

    def continuous_input_parser(self):
        print("### Unlimited Input Parser ###")
        self.hostname = self.get_username()
        
        try:
            parser = UnlimitedParser(FILE, self.hostname)
            parser.run()
        except Exception as e:
            print(f'An error occurred: {str(e)}')

    def select_option(self):
        options = {
            1: 'Parse the data with a time_init, time_end',
            2: 'Unlimited Input Parser'
        }

        option = self.get_option(options)

        if option == 1:
            self.parse_data_init_end_time()
        elif option == 2:
            self.continuous_input_parser()

if __name__ == '__main__':
    if os.path.isfile(FILE):
        try:
            menu = Menu()
            menu.select_option()
        except Exception as e:
            print(f'An error occurred during execution: {str(e)}')
    else:
        print('The log file does not exist. Please check the file path.')