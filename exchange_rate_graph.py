from datetime import datetime
from dateutil import relativedelta

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class ExchangeRateGraph:
    def __init__(self, graph_formatter, currency_exchange_rate_df):
        self.graph_formatter = graph_formatter
        self.currency_exchange_rate_df = currency_exchange_rate_df

    def create_graph_based_on_graph_formatter(self):
        date_of_today = pd.to_datetime(datetime.now().date())
        if self.graph_formatter == 'MONTH':
            self.graph_month_format(date_of_today)
        self.set_plot_settings()
        plt.show()

    def graph_month_format(self, date_of_today):
        currency_exchange_rate_df = self.currency_exchange_rate_df
        range_start_date = pd.to_datetime(date_of_today - relativedelta.relativedelta(months=1))
        sliced_exchange_rate_df = currency_exchange_rate_df[(currency_exchange_rate_df['DATE'] >= range_start_date)
                                                            & (currency_exchange_rate_df['DATE'] <= date_of_today)]
        graph = self.create_graph_from_df(sliced_exchange_rate_df)
        graph.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.SU))
        self.set_graph_ticks_formatter(graph)

    @staticmethod
    def create_graph_from_df(currency_exchange_rate_df):
        graph = currency_exchange_rate_df.plot(kind='line',
                                                    x='DATE',
                                                    y='US DOLLAR',
                                                    color='blue',
                                                    title='Currency Rate',
                                                    figsize=(15, 10),
                                                    grid=True)
        return graph

    @staticmethod
    def set_graph_ticks_formatter(graph):
        graph.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%Y'))

    @staticmethod
    def set_plot_settings():
        plt.ylabel("Rate")
        plt.xlabel("Date")
        plt.legend(['Date, Currency rate'])
