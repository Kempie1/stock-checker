#Some Notes from Max

#Is there a way to break your backend 
#figure out why the test coverage does not make the project 100% save 
#how does test coverage work
#The best test is the one that saves you time 
#You are done writting test when the test takes longer to write than the code itself 
#an api is a not a user interface it is an interface for the programmer

#https://stockcheckerdb.herokuapp.com/

#OTHER
import requests
import json
import psycopg2
import psycopg2.extras
import json
import jsonpath
import unittest
import os
from decouple import config
import sys
sys.path.append(config('ORMLogic'))
sys.path.append(config('APIFOLDER'))

#INTERNAL
from services import real_api_request
from constants import ticker_symbol_for_testing, ticker_symbol_for_request, ticker_symbol_table_full, ticker_symbol_table_empty, ticker_symbol_not_in_table
#EXTERNAL
from ORMLogic import api_call_to_json, ORM_services

class test_Api_Integration(unittest.TestCase):

    def test_api_request_status(self):
        #Arrange
        constant_input = ticker_symbol_for_request
        #Act
        response = real_api_request()
        #Assert
        self.assertEqual(response.status_code, 200)

    def test_json_getting_json_format(self):
        response = real_api_request()
        self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_api_data_ticker_symbol(self):
        response = real_api_request()
        response_body = response.json()
        self.assertEqual(response_body["ticker_symbol"], ticker_symbol_for_testing)

    def test_api_data_length_ticker_symbol(self):
        response = real_api_request()
        response_body = response.json()
        #As TSLA is 4 long
        self.assertEqual(len(response_body["ticker_symbol"]), 4)

    def test_respose_keys(self):
        response = real_api_request()
        response_body = response.json()
        response_keys = []
        for key in response_body:
            response_keys.append(key)
        list_of_keys = ['ask', 'ask_size', 'averagevolume', 'avg_vol_ten_day', 'avg_volume_3_month', 'beta', 'beta_5y_monthly', 'bid', 'bid_size', 'book_value_per_share_mrq', 'current_ratio_mrq', 'days_range_high', 'days_range_low', 'dividend_date', 'earnings_date', 'ebitda', 'eps_ttm', 'ex_dividend_date', 'fifty_day_moving_average', 'fifty_two_week_change', 'fifty_two_week_high', 'fifty_two_week_low', 'fifty_two_week_range_high', 'fifty_two_week_range_low', 'fiscal_year_ends', 'five_year_average_dividend_yield', 'forward_annual_dividend_rate', 'forward_annual_dividend_yield', 'gross_profit', 'levered_free_cash_flow_ttm', 'market_cap', 'most_recent_quarter_mrq', 'net_income_avi_to_common_ttm', 'one_year_target_est', 'open_bid', 'operating_cash_flow_ttm', 'operating_margin_ttm', 'payout_ratio', 'pe_ratio_ttm', 'previous_close', 'profit_margin', 'quarterly_earnings_growth_yoy', 'quarterly_revenue_growth_yoy', 'return_on_assets_ttm', 'return_on_equity_ttm', 'revenue_per_share_ttm', 'stock_name', 'stock_price', 'ticker_symbol', 'total_cash_mrq', 'total_cash_per_share_mrq', 'total_debt_divided_equity_mrq', 'total_debt_mrq', 'total_revenue', 'trailing_annual_dividend_rate', 'trailing_annual_dividend_yield', 'two_hundred_day_moving_average', 'volume']
        self.assertEqual(list_of_keys,response_keys)

if __name__ == '__main__':
    unittest.main()

#test_Api_Integration = test_Api_Integration()
#test_Api_Integration.test_something()