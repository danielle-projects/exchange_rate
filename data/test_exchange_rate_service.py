import os

from data.input_handler import InputHandler


class TestExchangeRateService:
    @staticmethod
    def test_is_file_exist_in_dir():
        file_name = 'test_file.txt'
        is_file_exist = InputHandler.is_file_exist_in_dir(file_name)
        if not is_file_exist:
            open(file_name, 'wb')
        is_file_exist = InputHandler.is_file_exist_in_dir(file_name)
        assert is_file_exist

    @staticmethod
    def test_remove_old_exchange_rate_files():
        file_name = 'test_file.txt'
        InputHandler.remove_old_exchange_rate_files(pattern=file_name)
        is_file_exist = InputHandler.is_file_exist_in_dir(file_name)
        assert not is_file_exist

    def test_convert_files_to_df(self):
        dir_name = 'test'
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        empty_file_name = 'empty_file.xslx'
        empty_df = self.create_empty_df_from_file(empty_file_name)

        non_exist_file_name = 'non_exist_file.txt'
        df_from_non_exist_file = self.create_df_from_non_exists_file(non_exist_file_name)

        file_name_csv = 'csv_file.csv'
        empty_df_from_csv = self.create_empty_df_from_file(file_name_csv)

        assert empty_df_from_csv.empty
        assert empty_df.empty
        assert df_from_non_exist_file.empty

    @staticmethod
    def create_file(full_path):
        open(full_path, 'wb')

    @staticmethod
    def create_empty_df_from_file(file_name):
        full_path = f'test/{file_name}'
        TestExchangeRateService.create_file(full_path)
        empty_df = InputHandler.convert_input_file_to_df(input_file=full_path)
        os.remove(full_path)
        return empty_df

    @staticmethod
    def create_df_from_non_exists_file(file_name):
        full_path = f'mock_files/{file_name}'
        df_from_non_exist_df = InputHandler.convert_input_file_to_df(input_file=full_path)
        return df_from_non_exist_df
