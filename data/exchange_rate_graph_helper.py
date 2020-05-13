from dateutil import relativedelta

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class ExchangeRateGraphHelper:

    @staticmethod
    def create_graph_month_format(date_of_today, currency_exchange_rate_df):
        range_start_date = pd.to_datetime(date_of_today - relativedelta.relativedelta(months=1))
        sliced_exchange_rate_df = currency_exchange_rate_df[(currency_exchange_rate_df['DATE'] >= range_start_date)
                                                            & (currency_exchange_rate_df['DATE'] <= date_of_today)]
        graph = ExchangeRateGraphHelper.create_graph_from_df(sliced_exchange_rate_df)
        graph.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.SU))

    @staticmethod
    def create_graph_week_format(date_of_today, currency_exchange_rate_df):
        range_start_date = pd.to_datetime(date_of_today - relativedelta.relativedelta(weeks=1))
        sliced_exchange_rate_df = currency_exchange_rate_df[(currency_exchange_rate_df['DATE'] >= range_start_date)
                                                            & (currency_exchange_rate_df['DATE'] <= date_of_today)]
        graph = ExchangeRateGraphHelper.create_graph_from_df(sliced_exchange_rate_df)
        graph.xaxis.set_major_locator(mdates.DayLocator())

    @staticmethod
    def create_graph_three_month_format(date_of_today, currency_exchange_rate_df):
        range_start_date = pd.to_datetime(date_of_today - relativedelta.relativedelta(months=3))
        sliced_exchange_rate_df = currency_exchange_rate_df[(currency_exchange_rate_df['DATE'] >= range_start_date)
                                                            & (currency_exchange_rate_df['DATE'] <= date_of_today)]
        graph = ExchangeRateGraphHelper.create_graph_from_df(sliced_exchange_rate_df)
        graph.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.SU))

    @staticmethod
    def create_graph_one_year_format(date_of_today, currency_exchange_rate_df):
        range_start_date = pd.to_datetime(date_of_today - relativedelta.relativedelta(years=1))
        sliced_exchange_rate_df = currency_exchange_rate_df[(currency_exchange_rate_df['DATE'] >= range_start_date)
                                                            & (currency_exchange_rate_df['DATE'] <= date_of_today)]
        graph = ExchangeRateGraphHelper.create_graph_from_df(sliced_exchange_rate_df)
        graph.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=date_of_today.day))
        ExchangeRateGraphHelper.set_plot_settings()
        plt.show()

    @staticmethod
    def create_graph_from_df(currency_exchange_rate_df):
        graph = currency_exchange_rate_df.plot(kind='line',
                                                    x='DATE',
                                                    y='US DOLLAR',
                                                    color='blue',
                                                    title='Currency Rate',
                                                    figsize=(15, 10),
                                                    grid=True)
        ExchangeRateGraphHelper.set_graph_ticks_formatter(graph)
        return graph

    @staticmethod
    def set_graph_ticks_formatter(graph):
        graph.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%Y'))

    @staticmethod
    def set_plot_settings():
        plt.ylabel("Rate")
        plt.xlabel("Date")
        plt.legend(['Date, Currency rate'])
