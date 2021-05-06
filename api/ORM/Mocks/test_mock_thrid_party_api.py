import requests
import unittest
from decouple import config
import sys
sys.path.append(config('ORM'))
sys.path.append(config('ORMLogic'))
sys.path.append(config('MockFolder'))
sys.path.append(config('APIFOLDER'))
import json
from ORM import services
from ORM import constants

class test_Mock_Third_Party_Api(unittest.TestCase):
    
    def test_mock_third_party_api_status(self):
        #Act
        response = services.mock_third_party_api_request()
        #Assert
        self.assertEqual(response.status_code, 200)
    
    def test_mock_third_party_api_getting_json_format(self):
        response = services.mock_third_party_api_request()
        self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_mock_third_party_api_data_length_ticker_symbol(self):
        response = services.mock_third_party_api_request()
        response_body = response.json()
        self.assertEqual(len(response_body['get-statistics']['symbol']), 4)

    def test_mock_third_party_api_data(self):
        #Act
        response = services.mock_third_party_api_request()
        #Assert
        response_body = response.json()
        self.assertEqual(response_body['get-statistics']['symbol'], constants.ticker_symbol_for_testing)

    def test_mock_third_party_api_dict_keys(self):
        response = services.mock_third_party_api_request()
        response_body = response.json()
        response_keys = []
        for key in response_body:
            response_keys.append(key)
        list_of_keys = ['get-financials', 'get-statistics']
        self.assertEqual(list_of_keys,response_keys)

    def test_mock_third_party_api_dict_financials_keys(self):
        list_financial_keys = ['balanceSheetHistory', 'balanceSheetHistoryQuarterly', 'cashflowStatementHistory', 'cashflowStatementHistoryQuarterly', 'earnings', 'errorList', 'financialsTemplate', 'incomeStatementHistory', 'incomeStatementHistoryQuarterly', 'loading', 'meta', 'pageViews', 'price', 'quoteType', 'summaryDetail', 'symbol', 'timeSeries']
        response = services.mock_third_party_api_request()
        response_body = response.json()
        response_keys = []
        for key in response_body['get-financials']:
            response_keys.append(key)
        self.assertEqual(list_financial_keys,response_keys)

    def test_mock_third_party_api_dict_statistics_keys(self):
        list_statistics_keys = ['calendarEvents', 'defaultKeyStatistics', 'financialData', 'financialsTemplate', 'mktmData', 'pageViews', 'price', 'quoteData', 'quoteType', 'summaryDetail', 'symbol']
        #print(response_body['get-statistics']['calendarEvents'].keys())
        response = services.mock_third_party_api_request()
        response_body = response.json()
        response_keys = []
        for key in response_body['get-statistics']:
            response_keys.append(key)
        self.assertEqual(list_statistics_keys,response_keys)

    def test_mock_teststock_json_data(self):
        #Act
        with open('ORM/teststock.json') as json_file:
            request_json = json.load(json_file)
        #Assert    
        self.assertEqual(request_json['get-statistics']['symbol'], constants.ticker_symbol_for_testing)

if __name__ == '__main__':
    unittest.main()
