#External
import requests
import json
import psycopg2
import psycopg2.extras
import json
import jsonpath
import unittest
import os
import sys
sys.path.append('/home/kempie/Projects/stock-checker/api/ORM/ORMLogic')
sys.path.append('/home/kempie/Projects/stock-checker/api/ORM')
sys.path.append('/home/kempie/Projects/stock-checker/api/')

#INTERNAL
from services import real_api_request
from constants import ticker_symbol_for_testing, ticker_symbol_for_request, ticker_symbol_table_full, ticker_symbol_table_empty, ticker_symbol_not_in_table
from main_execute import Execute

class test_Api_python_file(unittest.TestCase):
    #dependcy injection
    #This is now giving a return to the function

    #This function realies on the input fucntion which is a dependcy so I need to mock the user_input
    def test_user_input(self):
        #Arrange
        Main_function = Execute()
        #Act
        ticker_symbol_from_user = Main_function.user_input(self.mock_user_input())
        #Assert
        self.assertEqual(ticker_symbol_from_user, "['Some User Input']")

    def mock_user_input(self):
        return "Some User Input"

if __name__ == '__main__':
    unittest.main()