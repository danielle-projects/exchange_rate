from data.exchange_rate_graph_helper import ExchangeRateGraphHelper
from data.exchange_rate_graph_format import ExchangeRateGraphFormat


class ExchangeRateGraph:
    def __init__(self, graph_formatter, currency_code, currency_exchange_rate_df, date_of_today):
        self.graph_formatter = graph_formatter
        self.currency_code = currency_code
        self.currency_exchange_rate_df = currency_exchange_rate_df
        self.date_of_today = date_of_today

    def create_graph_based_on_graph_formatter(self):
        if self.graph_formatter == ExchangeRateGraphFormat.MONTH:
            ExchangeRateGraphHelper.process_graph_month_format(self.date_of_today, self.currency_code, self.currency_exchange_rate_df)
        elif self.graph_formatter == ExchangeRateGraphFormat.WEEK:
            ExchangeRateGraphHelper.create_graph_week_format(self.date_of_today, self.currency_code, self.currency_exchange_rate_df)
        elif self.graph_formatter == ExchangeRateGraphFormat.THREE_MONTHS:
            ExchangeRateGraphHelper.create_graph_three_month_format(self.date_of_today, self.currency_code, self.currency_exchange_rate_df)
        elif self.graph_formatter == ExchangeRateGraphFormat.ONE_YEAR:
            ExchangeRateGraphHelper.create_graph_one_year_format(self.date_of_today, self.currency_code, self.currency_exchange_rate_df)
        ExchangeRateGraphHelper.show_graph()
