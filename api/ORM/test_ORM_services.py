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
sys.path.append('/Users/maximilianhues/Documents/CODE/stock-checker/api/ORM/ORMLogic')

#INTERNAL
from services import real_api_request
from constants import ticker_symbol_for_testing, ticker_symbol_for_request, ticker_symbol_table_full, ticker_symbol_table_empty, ticker_symbol_not_in_table
#EXTERNAL
from ORMLogic import api_call_to_json, ORM_services


class test_Api_python_file(unittest.TestCase):
    #Dependcy Injection

    #This function realies on the input fucntion which is a dependcy so I need to mock the user_input
    def test_user_input(self):
        #Arrange
        Api_function = api_call_to_json.Api_call()
        #Act
        ticker_symbol_from_user = Api_function.user_input(self.mock_user_input())
        #Assert
        self.assertEqual(ticker_symbol_from_user, "['Some User Input']")

    def mock_user_input(self):
        return "Some User Input"

    def test_checking_if_table_is_empty(self):
        #Arrange
        services = ORM_services.ORM_services()
        #Act
        empty_table_check = services.checking_if_ticker_exists(ticker_symbol_for_request, ticker_symbol_table_empty)
        #Assert
        self.assertEqual(empty_table_check, False)

    def test_checking_if_ticker_does_not_exists(self):
        #Arrange
        services = ORM_services.ORM_services()
        #Act
        ticker_does_not_exists = services.checking_if_ticker_exists(ticker_symbol_not_in_table, ticker_symbol_table_full)
        #Assert
        self.assertEqual(ticker_does_not_exists, False)

    def test_checking_if_ticker_exists(self):
        #Arrange
        services = ORM_services.ORM_services()
        #Act
        table_full_check = services.checking_if_ticker_exists(ticker_symbol_for_request, ticker_symbol_table_full)
        #Assert
        self.assertEqual(table_full_check, True)


#if __name__ == '__main__':
  #  unittest.main()

Api_file_test = test_Api_python_file()
#Api_file_test.test_user_input()
Api_file_test.test_checking_if_table_is_empty()
#Api_file_test.test_checking_if_ticker_does_not_exists()
#Api_file_test.test_checking_if_ticker_exists()
#Api_file_test.test_api_request()