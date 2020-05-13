from datetime import datetime

import pandas as pd

from data.exchange_rate_graph_helper import ExchangeRateGraphHelper
from data.exchange_rate_graph_formatter import ExchangeRateGraphFormatter


class ExchangeRateGraph:
    def __init__(self, graph_formatter, currency_exchange_rate_df):
        self.graph_formatter = graph_formatter
        self.currency_exchange_rate_df = currency_exchange_rate_df
        self.date_of_today = pd.to_datetime(datetime.now().date())

    def create_graph_based_on_graph_formatter(self):
        currency_exchange_rate_df = self.currency_exchange_rate_df
        if self.graph_formatter == ExchangeRateGraphFormatter.MONTH:
            ExchangeRateGraphHelper.create_graph_month_format(self.currency_exchange_rate_df)
        elif self.graph_formatter == ExchangeRateGraphFormatter.WEEK:
            ExchangeRateGraphHelper.create_graph_week_format(self.currency_exchange_rate_df)
        elif self.graph_formatter == ExchangeRateGraphFormatter.THREE_MONTHS:
            ExchangeRateGraphHelper.create_graph_three_month_format(self.currency_exchange_rate_df)
        elif self.graph_formatter == ExchangeRateGraphFormatter.ONE_YEAR:
            ExchangeRateGraphHelper.create_graph_one_year_format(self.date_of_today, self.currency_exchange_rate_df)
        # ExchangeRateGraphHelper.set_plot_settings()
        # plt.show()
