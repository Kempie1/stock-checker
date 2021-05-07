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
from services import third_party_api_request
from constants import ticker_symbol_for_testing, ticker_symbol_for_request, ticker_symbol_table_full, ticker_symbol_table_empty, ticker_symbol_not_in_table
#EXTERNAL
from ORMLogic import api_call_to_json, ORM_services

class test_Third_Party_Api_Integration(unittest.TestCase):

    #This Test should have probally be in the server itself
    def test_real_third_party_api_request_status(self):
        #Act
        request = ["get-statistics", "get-financials", "get-chart"]
        for i in request:
            response = third_party_api_request(i)
            #Assert
            self.assertEqual(response.status_code, 200)
        
    def test_third_party_api_format(self):
        request = ["get-statistics", "get-financials", "get-chart"]
        for i in request:
            response = third_party_api_request(i)
            self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_api_data(self):
         #Act
        response1 = third_party_api_request("get-statistics")
        response2 = third_party_api_request("get-financials")
        response3 = third_party_api_request("get-chart")
        response1_json = response1.json()
        response2_json = response2.json()
        response3_json = response3.json()
        #Assert
        self.assertEqual(response1_json['symbol'], ticker_symbol_for_testing)
        self.assertEqual(response2_json['symbol'], ticker_symbol_for_testing)
        self.assertEqual(response3_json['chart']['result'][0]['meta']['symbol'], ticker_symbol_for_testing)

    def test_api_main_keys(self):
        request = ["get-statistics", "get-financials", "get-chart"]
        dict_statistics = {}
        dict_financials = {}
        dict_chart = {}
        for i in request:
            response = third_party_api_request(i)
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
        response = third_party_api_request("get-statistics")
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
        response = third_party_api_request("get-financials")
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
        response = third_party_api_request("get-chart")
        response_json = response.json()
        dict_chart = {}
        dict_chart["get-chart"] = response_json
        list_of_keys_main_chart = []
        for key, value in dict_chart.items():
            for keys, values in dict_chart[key].items():
                list_of_keys_main_chart.append(keys)
        expected_keys = ['chart']
        self.assertEqual(list_of_keys_main_chart, expected_keys)

    def test_json_data(self):
        #Arrange
        constant_input = ticker_symbol_for_testing
        #Act
        with open('ORM/teststock.json') as json_file:
            request_json = json.load(json_file)
            ticker_symbol_json = request_json['get-statistics']['symbol']
        #Assert    
        self.assertEqual(ticker_symbol_json, constant_input)

if __name__ == '__main__':
    unittest.main()

#Api_Integration_test = test_Third_Party_Api_Integration()
#Api_Integration_test.test_api_data()
#Api_Integration_test.test_api_data()
#Api_Integration_test.test_json_data()