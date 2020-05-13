import argparse

from datetime import datetime

from data.input_handler import InputHandler
from data.exchange_rate_graph import ExchangeRateGraph
from data.exchange_rate_graph_formatter import ExchangeRateGraphFormatter

default_start_date = datetime.now().date()

parser = argparse.ArgumentParser()
parser.add_argument('--currency', type=str, default='Dollar', choices=['Dollar'],
                    help='select a currency')
parser.add_argument('--graph_formatter',
                    type=str,
                    help='choose graph format',
                    default=ExchangeRateGraphFormatter.MONTH,
                    choices=[ExchangeRateGraphFormatter.WEEK,
                             ExchangeRateGraphFormatter.MONTH,
                             ExchangeRateGraphFormatter.THREE_MONTHS,
                             ExchangeRateGraphFormatter.ONE_YEAR])
args = parser.parse_args()

if __name__ == '__main__':
    input_handler = InputHandler(args.currency, args.graph_formatter)
    currency_exchange_rate_df = input_handler.convert_input_file_to_df()
    ExchangeRateGraph(args.graph_formatter, currency_exchange_rate_df)\
        .create_graph_based_on_graph_formatter()

