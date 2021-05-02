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


class test_Third_Party_Api_Integration(unittest.TestCase):

    #This Test should have probally be in the server itself
    def test_api_request_status(self):
        #Arrange
        constant_input = ticker_symbol_for_request
        #Act
        response = real_api_request()
        #Assert
        self.assertEqual(response.status_code, 200)
        
    def test_api_data(self):
        #Arrange
        constant_input = ticker_symbol_for_request
        #Act
        response = real_api_request()
        #Assert
        json_response = json.loads(response.text)
        ticker_symbol_from_API = jsonpath.jsonpath(json_response, 'symbol')
        self.assertEqual(ticker_symbol_from_API, constant_input)
    
    def test_json_data(self):
        #Arrange
        constant_input = ticker_symbol_for_testing
        #Act
        with open('ORM/teststock.json') as json_file:
            request_json = json.load(json_file)
            ticker_symbol_json = request_json['get-statistics']['symbol']
        #Assert    
        self.assertEqual(ticker_symbol_json, constant_input)

#if __name__ == '__main__':
    #unittest.main()

#Api_Integration_test = test_Third_Party_Api_Integration()
#Api_Integration_test.test_api_request_status()
#Api_Integration_test.test_api_data()
#Api_Integration_test.test_json_data()