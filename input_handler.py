import pandas as pd

from datetime import datetime

from dateutil import relativedelta

from exchange_rate_consts import ExchangeRateConsts


class InputHandler:
    def __init__(self, currency, graph_formatter):
        self.input_file_path = ExchangeRateConsts.EXCHANGE_RATE_INPUT_FILE
        self.currency = currency
        # self.start_date = pd.to_datetime(start_date)
        # self.end_date = pd.to_datetime(end_date)
        self.graph_formatter = graph_formatter
        self.currency_rate_df = self.convert_input_file_to_df()

    def convert_input_file_to_df(self):
        exchange_rate_df = pd.read_excel(self.input_file_path)
        return exchange_rate_df


