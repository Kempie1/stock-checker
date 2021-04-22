#OTHER
import requests
import json
import psycopg2
import psycopg2.extras
import json
import jsonpath
import unittest
import os
import sys
#This is needed to have acess to the ORM folder
#sys.path.insert(1, '/Users/maximilianhues/Documents/CODE/stock-checker/api/ORM')
sys.path.append('/Users/maximilianhues/Documents/CODE/stock-checker/api/ORM')

#INTERNAL
from services import real_api_request, get_uncompleted_todos
from constants import ticker_symbol_for_testing, ticker_symbol_for_request, ticker_symbol_table_full, ticker_symbol_table_empty, ticker_symbol_not_in_table
#EXTERNAL
from api_call_to_json import user_input

class test_Api_Integration(unittest.TestCase):

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
        with open('TestCases/teststock.json') as json_file:
            request_json = json.load(json_file)
            ticker_symbol_json = request_json['get-statistics']['symbol']
        #Assert    
        self.assertEqual(ticker_symbol_json, constant_input)

#if __name__ == '__main__':
    #unittest.main()

#Api_Integration_test = test_Api_Integration()
#Api_Integration_test.test_api_request_status()
#Api_Integration_test.test_api_data()
#Api_Integration_test.test_json_data()



class test_Api_python_file(unittest.TestCase):

    #dependcy injection
    #This is now giving a return to the function

    #This function realies on the input fucntion which is a dependcy so I need to mock the user_input
    def test_user_input(self):
        #Act
        ticker_symbol_from_user = user_input(self.mock_user_input)
        #Assert
        self.assertEqual(ticker_symbol_from_user, "['Some User Input']")

    def mock_user_input():
        return "Some User Input"

    def test_checking_if_ticker_exists(self):
        print(ticker_symbol_for_request)
        print(ticker_symbol_not_in_table)
        print(ticker_symbol_table_full)
        print(ticker_symbol_table_empty)
        print(len(ticker_symbol_table_full))
        print(len(ticker_symbol_table_empty))



Api_file_test = test_Api_python_file()
Api_file_test.test_user_input()
#Api_file_test.test_checking_if_ticker_exists()

