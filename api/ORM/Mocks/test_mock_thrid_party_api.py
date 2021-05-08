import requests
import unittest
from decouple import config
import sys
sys.path.append(config('ORM'))
sys.path.append(config('ORMLogic'))
sys.path.append(config('MockFolder'))
sys.path.append(config('APIFOLDER'))
import json
import pytest
from ORM import services
from ORM import constants

#@pytest.mark.mock
@pytest.mark.skip(reason="I dont want to run this test at the moment")
class test_Mock_Third_Party_Api(unittest.TestCase):
    
    def test_mock_third_party_api_status(self):
        #Act
        request = ["get-statistics", "get-financials", "get-chart"]
        for i in request:
            response = services.mock_third_party_api_request(i)
            #Assert
            self.assertEqual(response.status_code, 200)
    
    def test_mock_third_party_api_getting_json_format(self):
        request = ["get-statistics", "get-financials", "get-chart"]
        for i in request:
            response = services.mock_third_party_api_request(i)
            self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_mock_third_party_api_data(self):
        #Act
        request = ["get-statistics", "get-financials", "get-chart"]
        for i in request:
            response = services.mock_third_party_api_request(i)
            response_body = response.json()

        #Act
        response1 = services.mock_third_party_api_request("get-statistics")
        response2 = services.mock_third_party_api_request("get-financials")
        response3 = services.mock_third_party_api_request("get-chart")
        response1_json = response1.json()
        response2_json = response2.json()
        response3_json = response3.json()
        #Assert
        json_response = response.json()
        self.assertEqual(response1_json['symbol'], services.ticker_symbol_for_testing)
        self.assertEqual(response2_json['symbol'], services.ticker_symbol_for_testing)
        self.assertEqual(response3_json['chart']['result'][0]['meta']['symbol'], services.ticker_symbol_for_testing)

    def test_mock_third_party_api_main_dict_keys(self):
        request = ["get-statistics", "get-financials", "get-chart"]
        dict_statistics = {}
        dict_financials = {}
        dict_chart = {}
        for i in request:
            response = services.mock_third_party_api_request(i)
            response_json = response.json()
            if i == "get-statistics":
                dict_statistics["get-statistics"] = response_json
            if i == "get-financials":
                dict_financials["get-financials"] = response_json
            if i == "get-chart":
                dict_chart["get-chart"] = response_json
        merge_all_dicts = {**dict_statistics, **dict_financials, **dict_chart}
        expected_keys = "dict_keys(['get-statistics', 'get-financials', 'get-chart'])"
        response_keys = str(merge_all_dicts.keys())
        self.assertEqual(expected_keys, response_keys)    

    
    def test_api_statistics_nested_keys(self):
        response = services.mock_third_party_api_request("get-statistics")
        response_json = response.json()
        dict_statistics = {}
        dict_statistics["get-statistics"] = response_json
        list_of_keys_main_statistics = []
        for key, value in dict_statistics.items():
            for keys, values in dict_statistics[key].items():
                list_of_keys_main_statistics.append(keys)
        expected_keys = ['defaultKeyStatistics', 'financialsTemplate', 'price', 'financialData', 'quoteType', 'calendarEvents', 'summaryDetail', 'symbol', 'pageViews', 'quoteData', 'mktmData']
        self.assertEqual(list_of_keys_main_statistics, expected_keys)

    def test_api_financials_nested_keys(self):
        response = services.mock_third_party_api_request("get-financials")
        response_json = response.json()
        dict_financials = {}
        dict_financials["get-financials"] = response_json
        list_of_keys_main_financials = []
        for key, value in dict_financials.items():
            for keys, values in dict_financials[key].items():
                list_of_keys_main_financials.append(keys)
        expected_keys = ['financialsTemplate', 'cashflowStatementHistory', 'balanceSheetHistoryQuarterly', 'earnings', 'price', 'incomeStatementHistoryQuarterly', 'incomeStatementHistory', 'balanceSheetHistory', 'cashflowStatementHistoryQuarterly', 'quoteType', 'summaryDetail', 'symbol', 'pageViews', 'timeSeries', 'meta', 'loading', 'errorList']
        self.assertEqual(list_of_keys_main_financials, expected_keys)

    def test_api_chart_nested_keys(self):
        response = services.mock_third_party_api_request("get-chart")
        response_json = response.json()
        dict_chart = {}
        dict_chart["get-chart"] = response_json
        list_of_keys_main_chart = []
        for key, value in dict_chart.items():
            for keys, values in dict_chart[key].items():
                list_of_keys_main_chart.append(keys)
        expected_keys = ['chart']
        self.assertEqual(list_of_keys_main_chart, expected_keys)

    def test_mock_teststock_json_data(self):
        #Act
        with open('ORM/teststock.json') as json_file:
            request_json = json.load(json_file)
        #Assert    
        self.assertEqual(request_json['get-statistics']['symbol'], constants.ticker_symbol_for_testing)

if __name__ == '__main__':
    unittest.main()

#mock_api = test_Mock_Third_Party_Api()
#mock_api.test_mock_third_party_api_data()