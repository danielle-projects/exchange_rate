from dateutil import relativedelta
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from data.currencies import Currencies
from data.exchange_rate_graph_consts import ExchangeRateGraphConsts


class ExchangeRateGraphHelper:
    @staticmethod
    def process_graph_month_format(date_of_today, currency_code, currency_exchange_rate_df):
        start_date = pd.to_datetime(date_of_today - relativedelta.relativedelta(months=1))
        graph = ExchangeRateGraphHelper.create_graph(start_date=start_date,
                                                     end_date=date_of_today,
                                                     currency_code=currency_code,
                                                     df=currency_exchange_rate_df)
        graph.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.SU))
        ExchangeRateGraphHelper.show_graph()

    @staticmethod
    def create_graph_week_format(date_of_today, currency_code, currency_exchange_rate_df):
        start_date = pd.to_datetime(date_of_today - relativedelta.relativedelta(weeks=1))
        graph = ExchangeRateGraphHelper.create_graph(start_date=start_date,
                                                     end_date=date_of_today,
                                                     currency_code=currency_code,
                                                     df=currency_exchange_rate_df)
        graph.xaxis.set_major_locator(mdates.DayLocator())
        ExchangeRateGraphHelper.show_graph()

    @staticmethod
    def create_graph_three_month_format(date_of_today, currency_code, currency_exchange_rate_df):
        start_date = pd.to_datetime(date_of_today - relativedelta.relativedelta(months=3))
        graph = ExchangeRateGraphHelper.create_graph(start_date=start_date,
                                                     end_date=date_of_today,
                                                     currency_code=currency_code,
                                                     df=currency_exchange_rate_df)
        graph.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.SU))
        ExchangeRateGraphHelper.show_graph()

    @staticmethod
    def create_graph_one_year_format(date_of_today, currency_code, currency_exchange_rate_df):
        start_date = pd.to_datetime(date_of_today - relativedelta.relativedelta(years=1))
        graph = ExchangeRateGraphHelper.create_graph(start_date=start_date,
                                                     end_date=date_of_today,
                                                     currency_code=currency_code,
                                                     df=currency_exchange_rate_df)
        graph.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=date_of_today.day))
        ExchangeRateGraphHelper.show_graph()

    @staticmethod
    def create_graph(start_date, end_date, currency_code, df):
        sliced_exchange_rate_df = df[(df[ExchangeRateGraphConsts.DATE_COLUMN_NAME] >= start_date)
                                     & (df[ExchangeRateGraphConsts.DATE_COLUMN_NAME] <= end_date)]
        graph = ExchangeRateGraphHelper.create_graph_from_df(sliced_exchange_rate_df, currency_code)
        return graph

    @staticmethod
    def create_graph_from_df(currency_exchange_rate_df, currency_code):
        relevant_currency_column_name = Currencies.get_currencies_dict()[currency_code]
        ax = plt.gca()
        graph = currency_exchange_rate_df.plot(kind=ExchangeRateGraphConsts.GRAPH_KIND,
                                               x=ExchangeRateGraphConsts.DATE_COLUMN_NAME,
                                               y=relevant_currency_column_name,
                                               color=ExchangeRateGraphConsts.GRAPH_COLOR,
                                               title=ExchangeRateGraphConsts.GRAPH_TITLE,
                                               figsize=ExchangeRateGraphConsts.FIGURE_SIZE,
                                               grid=ExchangeRateGraphConsts.GRAPH_GRID,
                                               ax=ax)
        graph.set_ylabel(ExchangeRateGraphConsts.PLOT_Y_LABEL)
        graph.set_xlabel(ExchangeRateGraphConsts.PLOT_X_LABEL)
        graph.legend(ExchangeRateGraphConsts.PLOT_LEGEND)
        ExchangeRateGraphHelper.set_graph_ticks_format(graph)
        return graph

    @staticmethod
    def set_graph_ticks_format(graph):
        graph.xaxis.set_major_formatter(mdates.DateFormatter(ExchangeRateGraphConsts.GRAPH_THICK_DATE_FORMAT))

    @staticmethod
    def show_graph():
        plt.show()
