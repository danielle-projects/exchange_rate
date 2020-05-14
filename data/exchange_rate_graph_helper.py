from dateutil import relativedelta
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from data.currencies import Currencies
from data.exchange_rate_graph_consts import ExchangeRateGraphConsts


class ExchangeRateGraphHelper:
    @staticmethod
    def process_graph(
            date_of_today,
            currency_code,
            currency_exchange_rate_df,
            ticker_locator,
            **kwargs,
    ):
        relative_delta = ExchangeRateGraphHelper.get_relativedelta(**kwargs)
        start_date = pd.to_datetime(date_of_today - relative_delta)
        ExchangeRateGraphHelper.create_graph(
            start_date=start_date,
            end_date=date_of_today,
            currency_code=currency_code,
            df=currency_exchange_rate_df,
            ticker_locator=ticker_locator,
        )

    @staticmethod
    def create_graph(start_date, end_date, currency_code, df, ticker_locator):
        sliced_exchange_rate_df = df[(df[ExchangeRateGraphConsts.DATE_COLUMN_NAME] >= start_date)
                                     & (df[ExchangeRateGraphConsts.DATE_COLUMN_NAME] <= end_date)]
        graph = ExchangeRateGraphHelper.create_graph_from_df(sliced_exchange_rate_df, currency_code)
        graph.xaxis.set_major_locator(ticker_locator)
        ExchangeRateGraphHelper.show_graph()

    @staticmethod
    def create_graph_from_df(currency_exchange_rate_df, currency_code):
        relevant_currency_column_name = Currencies.get_currencies_dict()[currency_code]
        ax = plt.gca()
        graph = currency_exchange_rate_df.plot(
            kind=ExchangeRateGraphConsts.GRAPH_KIND,
            x=ExchangeRateGraphConsts.DATE_COLUMN_NAME,
            y=relevant_currency_column_name,
            color=ExchangeRateGraphConsts.GRAPH_COLOR,
            title=ExchangeRateGraphConsts.GRAPH_TITLE,
            figsize=ExchangeRateGraphConsts.FIGURE_SIZE,
            grid=ExchangeRateGraphConsts.GRAPH_GRID,
            ax=ax,
        )
        graph.set_ylabel(ExchangeRateGraphConsts.PLOT_Y_LABEL)
        graph.set_xlabel(ExchangeRateGraphConsts.PLOT_X_LABEL)
        graph.legend(ExchangeRateGraphConsts.PLOT_LEGEND)
        graph.xaxis.set_major_formatter(mdates.DateFormatter(ExchangeRateGraphConsts.GRAPH_THICK_DATE_FORMAT))
        return graph

    @staticmethod
    def get_relativedelta(**kwargs):
        if 'months' in kwargs.keys():
            relative_delta = relativedelta.relativedelta(months=kwargs['months'])
        elif 'weeks' in kwargs.keys():
            relative_delta = relativedelta.relativedelta(weeks=kwargs['weeks'])
        else:
            relative_delta = relativedelta.relativedelta(years=kwargs['years'])
        return relative_delta

    @staticmethod
    def show_graph():
        plt.show()
