import pandas as pd

from data.exchange_rate_consts import ExchangeRateConsts


class InputHandler:
    def __init__(self, currency, graph_formatter):
        self.input_file_path = ExchangeRateConsts.EXCHANGE_RATE_INPUT_FILE
        self.currency = currency
        self.graph_formatter = graph_formatter
        self.currency_rate_df = self.convert_input_file_to_df()

    def convert_input_file_to_df(self):
        exchange_rate_df = pd.read_excel(self.input_file_path)
        return exchange_rate_df


