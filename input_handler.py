import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from exchange_rate_consts import ExchangeRateConsts


class InputHandler:
    def __init__(self, currency, start_date, end_date):
        self.input_file_path = ExchangeRateConsts.EXCHANGE_RATE_INPUT_FILE
        self.currency = currency
        self.start_date = start_date
        self.end_date = end_date

    def convert_input_file_to_df(self):
        exchange_rate_df = pd.read_excel(self.input_file_path)
        exchange_rate_df.sort_values(by='DATE', ascending=False, inplace=True)

        exchange_rate_df = exchange_rate_df.head(8)
        ax = exchange_rate_df.plot(kind='line', x='DATE', y='US DOLLAR', color='blue', title='Currency Rate',
                                   figsize=(15, 10))
        plt.ylabel("Rate")
        plt.xlabel("Date")
        plt.legend(['Date, Currency rate'])
        ax.xaxis.set_major_locator(mdates.DayLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%Y'))
        plt.show()
        print(exchange_rate_df)

    def slice_df_by_date_range(self, df):
        pass