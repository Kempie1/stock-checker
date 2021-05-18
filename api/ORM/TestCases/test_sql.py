import requests
import json
import psycopg2
import psycopg2.extras
import json
import jsonpath
import unittest
import os
import sys
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
#This is needed to have acess to the ORM folder
sys.path.append(config('ORMLogic'))
from services import real_api_request, real_sql_request
from constants import ticker_symbol_for_testing, ticker_symbol_for_request, ticker_symbol_table_full, ticker_symbol_table_empty, ticker_symbol_not_in_table
#EXTERNAL
from ORMLogic import json_to_server

class test_Sql_Integration(unittest.TestCase):
    def test_sql_connection(self):
        list_of_ticker_symbols = []
        engine = real_sql_request()
        with engine.connect() as connection:
            result = connection.execute(text("SELECT ticker_symbol FROM stock"))
            for row in result:
                list_of_ticker_symbols.append(row['ticker_symbol'])
        for i in list_of_ticker_symbols:
            if i == 'TSLA':
                self.assertEqual(i, 'TSLA')

    def test_colums_SQL(self):
        engine = real_sql_request()
        list_of_columns = []
        list_of_expected_columns = ['ticker_symbol', 'stock_name', 'stock_price', 'previous_close', 'open_bid', 'bid', 'bid_size', 'ask', 'ask_size', 'days_range_high', 'days_range_low', 'fifty_two_week_range_high', 'fifty_two_week_range_low', 'pe_ratio_ttm', 'eps_ttm', 'earnings_date', 'volume', 'avg_volume_3_month', 'market_cap', 'beta', 'one_year_target_est', 'ex_dividend_date', 'total_revenue', 'gross_profit', 'profit_margin', 'operating_margin_ttm', 'revenue_per_share_ttm', 'quarterly_revenue_growth_yoy', 'ebitda', 'net_income_avi_to_common_ttm', 'quarterly_earnings_growth_yoy', 'return_on_assets_ttm', 'return_on_equity_ttm', 'operating_cash_flow_ttm', 'levered_free_cash_flow_ttm', 'fiscal_year_ends', 'most_recent_quarter_mrq', 'total_cash_mrq', 'total_cash_per_share_mrq', 'total_debt_mrq', 'total_debt_divided_equity_mrq', 'current_ratio_mrq', 'book_value_per_share_mrq', 'beta_5y_monthly', 'fifty_two_week_change', 'averagevolume', 'fifty_two_week_high', 'fifty_two_week_low', 'fifty_day_moving_average', 'two_hundred_day_moving_average', 'avg_vol_ten_day', 'forward_annual_dividend_rate', 'forward_annual_dividend_yield', 'trailing_annual_dividend_rate', 'trailing_annual_dividend_yield', 'five_year_average_dividend_yield', 'payout_ratio', 'dividend_date']
        with engine.connect() as connection:
            result = connection.execute(text('''
            select column_name, data_type, character_maximum_length
            from INFORMATION_SCHEMA.COLUMNS
            where table_name = 'stock'
    '''))
            for row in result:
                list_of_columns.append(row['column_name'])
            self.assertEqual(list_of_columns, list_of_expected_columns)


#test_sql_integration = test_Sql_Integration()
#test_sql_integration.integration()

class test_Sql_python_file(unittest.TestCase):
    def test_open_json_file(self):
        json_to_server_class = json_to_server.Json_to_server()
        open_json = json_to_server_class.open_json_file(config('TestJson'))
        self.assertEqual(open_json, True)

if __name__ == '__main__':
    unittest.main()


#test_sql_python_file = test_Sql_python_file()
#test_sql_python_file.test_function()