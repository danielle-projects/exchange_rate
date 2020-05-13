import os
import requests
from datetime import datetime
import fnmatch

import pandas as pd
from bs4 import BeautifulSoup

from data.input_handler_conts import InputHandlerConsts


class InputHandler:
    def __init__(self, currency, graph_format):
        self.input_file_path = self.get_updated_file_path()
        self.currency = currency
        self.graph_format = graph_format
        self.currency_rate_df = self.convert_input_file_to_df()

    def get_updated_file_path(self):
        """
        check if exchange_rate.xlsx from today is already exists in current working dir.
        if not - get the data file from boi(bank of Israel website)
        :return:
        """
        date_of_today = datetime.now().date().strftime(InputHandlerConsts.DATE_FORMAT)
        file_name = InputHandlerConsts.CUSTOM_FILE_NAME.format(date_of_today)
        cur_dir = os.getcwd()
        if file_name not in os.listdir(cur_dir):
            self.remove_old_exchange_rate_files(cur_dir)
            self.get_exchange_rate_data_from_boi_website(file_name)
        return file_name

    def convert_input_file_to_df(self):
        exchange_rate_df = pd.read_excel(self.input_file_path)
        return exchange_rate_df

    def get_exchange_rate_data_from_boi_website(self, file_name):
        soup = self.get_boi_web_file_content()
        self.extract_exchange_rate_file(soup, file_name)

    @staticmethod
    def get_boi_web_file_content():
        url = InputHandlerConsts.BOI_EXCHANGE_RATE_URL
        try:
            res = requests.get(url)
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            raise
        except Exception as err:
            print(f'An error has occurred: {err}')
            raise
        soup = BeautifulSoup(res.content, features=InputHandlerConsts.HTML_PARSER)
        return soup

    @staticmethod
    def extract_exchange_rate_file(soup, file_name):
        tag = soup.select_one(
            f'a[href*={InputHandlerConsts.BOI_EXCHANGE_RATE_FILE_NAME}]')
        if tag is None:
            print(f'required file {InputHandlerConsts.BOI_EXCHANGE_RATE_FILE_NAME}.xlsx'
                  f' is not exist in {InputHandlerConsts.BOI_EXCHANGE_RATE_URL} url')
        try:
            periodic_exchange_rates_file_name = tag.attrs[InputHandlerConsts.HREF_ATTR]
            full_periodic_exchange_rates_url = "".join((InputHandlerConsts.BOI_BASE_URL,
                                                        str(periodic_exchange_rates_file_name)))
            resp = requests.get(full_periodic_exchange_rates_url)
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            raise
        except Exception as err:
            print(f'An error has occurred: {err}')
            raise
        output = open(file_name, mode='wb')
        output.write(resp.content)
        output.close()

    @staticmethod
    def remove_old_exchange_rate_files(cur_dir):
        for filename in fnmatch.filter(os.listdir(cur_dir), 'exchange_rate_*.xlsx'):
            try:
                os.remove(os.path.join(cur_dir, filename))
            except OSError:
                print("Error while deleting file")