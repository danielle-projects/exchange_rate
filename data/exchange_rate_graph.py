import matplotlib.dates as mdates

from data.exchange_rate_graph_helper import ExchangeRateGraphHelper
from data.exchange_rate_graph_format import ExchangeRateGraphFormat


class ExchangeRateGraph:
    def __init__(self, graph_format, currency_code, currency_exchange_rate_df, date_of_today):
        self.graph_format = graph_format
        self.currency_code = currency_code
        self.currency_exchange_rate_df = currency_exchange_rate_df
        self.date_of_today = date_of_today

    def create_graph_based_on_graph_format(self):
        if self.graph_format == ExchangeRateGraphFormat.MONTH:
            ticker_locator = mdates.WeekdayLocator(byweekday=mdates.SU)
            ExchangeRateGraphHelper.process_graph(
                self.date_of_today,
                self.currency_code,
                self.currency_exchange_rate_df,
                ticker_locator,
                months=1,
            )
        elif self.graph_format == ExchangeRateGraphFormat.WEEK:
            ticker_locator = mdates.DayLocator()
            ExchangeRateGraphHelper.process_graph(
                self.date_of_today,
                self.currency_code,
                self.currency_exchange_rate_df,
                ticker_locator,
                weeks=1,
            )
        elif self.graph_format == ExchangeRateGraphFormat.THREE_MONTHS:
            ticker_locator = mdates.WeekdayLocator(byweekday=mdates.SU)
            ExchangeRateGraphHelper.process_graph(
                self.date_of_today,
                self.currency_code,
                self.currency_exchange_rate_df,
                ticker_locator,
                months=3,
            )
        elif self.graph_format == ExchangeRateGraphFormat.ONE_YEAR:
            ticker_locator = mdates.MonthLocator(bymonthday=self.date_of_today.day)
            ExchangeRateGraphHelper.process_graph(
                self.date_of_today,
                self.currency_code,
                self.currency_exchange_rate_df,
                ticker_locator,
                years=1,
            )
