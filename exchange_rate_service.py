import argparse
import pandas as pd
from datetime import datetime

from data.input_handler import InputHandler
from data.exchange_rate_graph import ExchangeRateGraph
from data.exchange_rate_graph_format import ExchangeRateGraphFormat
from data.currencies import Currencies


class ExchangeRateService:
    def __init__(self):
        input_handler = InputHandler(args.currency, args.graph_formatter)
        self.currency_exchange_rate_df = input_handler.convert_input_file_to_df()
        if self.currency_exchange_rate_df.empty:
            print('currency exchange rate df is empty')
            return
        ExchangeRateGraph(graph_formatter=args.graph_formatter,
                          currency_code=args.currency,
                          currency_exchange_rate_df=self.currency_exchange_rate_df,
                          date_of_today=pd.to_datetime(datetime.now().date())) \
            .create_graph_based_on_graph_formatter()


if __name__ == '__main__':
    currency_codes = Currencies.get_currencies_dict()
    currencies_string = [f'{code} for {desc}' for code, desc in currency_codes.items()]
    parser = argparse.ArgumentParser()
    parser.add_argument('--currency',
                        type=str.upper,
                        default='USD',
                        choices=currency_codes.keys(),
                        help=f'''choose currency code - default is USD,
                             optional choices are {currencies_string}''')

    parser.add_argument('--graph_formatter',
                        type=str.lower,
                        help='choose graph format',
                        default=ExchangeRateGraphFormat.MONTH,
                        choices=[ExchangeRateGraphFormat.WEEK,
                                 ExchangeRateGraphFormat.MONTH,
                                 ExchangeRateGraphFormat.THREE_MONTHS,
                                 ExchangeRateGraphFormat.ONE_YEAR])
    args = parser.parse_args()
    ExchangeRateService()
