class InputHandlerConsts:
    DATE_FORMAT = '%d_%m_%Y'
    BOI_BASE_URL = 'https://www.boi.org.il'
    BOI_EXCHANGE_RATE_URL = ''.join((BOI_BASE_URL,
                                     '/he/Markets/ForeignCurrencyMarket/Pages/PeriodicExchangeRates.aspx'))
    BOI_EXCHANGE_RATE_FILE_NAME = 'yazigmizt'
    HREF_ATTR = 'href'
    CUSTOM_FILE_NAME = 'exchange_rate_{}.xlsx'
    EXCHANGE_RATE_FILE_PATTERN = 'exchange_rate_*.xlsx'
    SUCCESS_STATUS_CODE = '200'
    HTML_PARSER = 'html.parser'
