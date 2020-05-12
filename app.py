import argparse
import pandas as pd
# import xml.etree.ElementTree as ET
from input_handler import InputHandler
from datetime import datetime, timedelta

from input_handler import InputHandler

default_start_date = datetime.now().date()

parser = argparse.ArgumentParser()
parser.add_argument('--currency', type=str, default='Dollar', choices=['Dollar'],
                    help='select a currency')
parser.add_argument('--start-date', type=datetime.date, help='choose start date', default=datetime.now().date())
parser.add_argument('--end-date', type=datetime.date, help='choose end date',
                    default=datetime.now().date() - timedelta(month=1))
args = parser.parse_args()
print('')

if __name__ == '__main__':
    input_handler = InputHandler(args.currency, args.start_date, args.end_date)
    input_handler.convert_input_file_to_df()

