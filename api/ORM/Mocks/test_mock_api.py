import requests
import unittest
from decouple import config
import sys
import pytest

sys.path.append(config('ORM'))
sys.path.append(config('TestCases'))
sys.path.append(config('ORMLogic'))
sys.path.append(config('MockFolder'))
sys.path.append(config('APIFOLDER'))
from TestCases import services
from TestCases import constants

@pytest.mark.skip(reason="I dont want to run this test at the moment")
class test_Mock_Api(unittest.TestCase):
    
    def test_mock_api_request_status(self):
        #Act
        response = services.mock_api_request()
        #Assert
        self.assertEqual(response.status_code, 200)

    def test_mock_api_getting_json_format(self):
        #Act
        response = services.mock_api_request()
        #Assert
        self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_mock_api_data_ticker_symbol(self):
        #Act
        response = services.mock_api_request()
        response_body = response.json()
        #Assert
        self.assertEqual(response_body["ticker_symbol"], constants.ticker_symbol_for_testing)

    def test_mock_api_dict_keys(self):
        #Arrange
        response_keys = []
        list_of_keys = ['ask', 'ask_size', 'averagevolume', 'avg_vol_ten_day', 'avg_volume_3_month', 'beta', 'beta_5y_monthly', 'bid', 'bid_size', 'book_value_per_share_mrq', 'current_ratio_mrq', 'days_range_high', 'days_range_low', 'dividend_date', 'earnings_date', 'ebitda', 'eps_ttm', 'ex_dividend_date', 'fifty_day_moving_average', 'fifty_two_week_change', 'fifty_two_week_high', 'fifty_two_week_low', 'fifty_two_week_range_high', 'fifty_two_week_range_low', 'fiscal_year_ends', 'five_year_average_dividend_yield', 'forward_annual_dividend_rate', 'forward_annual_dividend_yield', 'gross_profit', 'levered_free_cash_flow_ttm', 'market_cap', 'most_recent_quarter_mrq', 'net_income_avi_to_common_ttm', 'one_year_target_est', 'open_bid', 'operating_cash_flow_ttm', 'operating_margin_ttm', 'payout_ratio', 'pe_ratio_ttm', 'previous_close', 'profit_margin', 'quarterly_earnings_growth_yoy', 'quarterly_revenue_growth_yoy', 'return_on_assets_ttm', 'return_on_equity_ttm', 'revenue_per_share_ttm', 'stock_name', 'stock_price', 'ticker_symbol', 'total_cash_mrq', 'total_cash_per_share_mrq', 'total_debt_divided_equity_mrq', 'total_debt_mrq', 'total_revenue', 'trailing_annual_dividend_rate', 'trailing_annual_dividend_yield', 'two_hundred_day_moving_average', 'volume']
        #Act
        response = services.mock_api_request()
        response_body = response.json()
        for key in response_body:
            response_keys.append(key)
        #Assert
        self.assertEqual(list_of_keys,response_keys)

if __name__ == '__main__':
    unittest.main()