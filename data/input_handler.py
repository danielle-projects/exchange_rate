import os
import requests
from datetime import datetime
import fnmatch
import logging

import pandas as pd
from bs4 import BeautifulSoup

from data.input_handler_conts import InputHandlerConsts


class InputHandler:
    def __init__(self):
        self.input_file_path = self.get_updated_file_path()
        self.currency_rate_df = self.convert_input_file_to_df(self.input_file_path)

    def get_updated_file_path(self):
        """
        check if exchange_rate.xlsx from today is already exists in current working dir.
        if not - get the data file from boi(bank of Israel website)
        :return:
        """
        date_of_today = datetime.now().date().strftime(InputHandlerConsts.DATE_FORMAT)
        file_name = InputHandlerConsts.CUSTOM_FILE_NAME.format(date_of_today)
        if not self.is_file_exist_in_dir(file_name):
            self.remove_old_exchange_rate_files()
            self.get_exchange_rate_data_from_boi_website(file_name)
        return file_name

    @staticmethod
    def convert_input_file_to_df(input_file):
        exchange_rate_df = pd.DataFrame()
        if InputHandler.is_file_exist_in_dir(input_file):
            exchange_rate_df = pd.read_excel(input_file)
        return exchange_rate_df

    def get_exchange_rate_data_from_boi_website(self, file_name):
        soup = self.get_boi_web_file_content()
        self.extract_exchange_rate_file(soup, file_name)

    @staticmethod
    def get_boi_web_file_content():
        response = None
        beautifulsoup = None
        url = InputHandlerConsts.BOI_EXCHANGE_RATE_URL
        try:
            response = requests.get(url)
        except requests.HTTPError as http_err:
            logging.warning(f'HTTP error occurred: {http_err}')
        except Exception as err:
            logging.warning(f'An error has occurred: {err}')
        if response:
            beautifulsoup = BeautifulSoup(response.content, features=InputHandlerConsts.HTML_PARSER)
        return beautifulsoup

    @staticmethod
    def extract_exchange_rate_file(beautifulsoup, file_name):
        response = None
        if beautifulsoup:
            tag = beautifulsoup.select_one(
                f'a[href*={InputHandlerConsts.BOI_EXCHANGE_RATE_FILE_NAME}]')
            if tag is None:
                logging.warning(f'required file {InputHandlerConsts.BOI_EXCHANGE_RATE_FILE_NAME}.xlsx'
                                f' is not exist in {InputHandlerConsts.BOI_EXCHANGE_RATE_URL} url')
            try:
                periodic_exchange_rates_file_name = tag.attrs[InputHandlerConsts.HREF_ATTR]
                full_periodic_exchange_rates_url = "".join((InputHandlerConsts.BOI_BASE_URL,
                                                            str(periodic_exchange_rates_file_name)))
                response = requests.get(full_periodic_exchange_rates_url)
            except requests.HTTPError as http_err:
                logging.info(f'HTTP error occurred: {http_err}')
            except Exception as err:
                logging.warning(f'An error has occurred: {err}')
        if response:
            output = open(file_name, mode='wb')
            output.write(response.content)
            output.close()

    @staticmethod
    def remove_old_exchange_rate_files(pattern=InputHandlerConsts.EXCHANGE_RATE_FILE_PATTERN):
        cur_dir = os.getcwd()
        for filename in fnmatch.filter(os.listdir(cur_dir), pattern):
            try:
                os.remove(os.path.join(cur_dir, filename))
            except OSError:
                logging.warning("Error while deleting file")

    @staticmethod
    def is_file_exist_in_dir(file_name, cur_dir=os.getcwd()):
        is_file_exists = False
        if file_name in os.listdir(cur_dir):
            is_file_exists = True
        return is_file_exists

