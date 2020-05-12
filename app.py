import argparse

from datetime import datetime
from dateutil import relativedelta

from input_handler import InputHandler
from exchange_rate_graph import ExchangeRateGraph

default_start_date = datetime.now().date()

parser = argparse.ArgumentParser()
parser.add_argument('--currency', type=str, default='Dollar', choices=['Dollar'],
                    help='select a currency')
parser.add_argument('--start-date', type=datetime.date, help='choose start date',
                    default=datetime.now().date() - relativedelta.relativedelta(months=1))
parser.add_argument('--end-date', type=datetime.date, help='choose end date',
                    default=datetime.now().date())
parser.add_argument('--graph_formatter', type=str, help='choose range',
                    default='MONTH', choices=['WEEK, MONTH, 3 MONTH, ONE YEAR'])
args = parser.parse_args()

if __name__ == '__main__':
    input_handler = InputHandler(args.currency, args.graph_formatter)
    currency_exchange_rate_df = input_handler.convert_input_file_to_df()
    ExchangeRateGraph(args.graph_formatter, currency_exchange_rate_df)\
        .create_graph_based_on_graph_formatter()

