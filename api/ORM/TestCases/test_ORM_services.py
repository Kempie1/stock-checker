#External
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

#INTERNAL
from services import real_api_request
from constants import ticker_symbol_for_testing, ticker_symbol_for_request, ticker_symbol_table_full, ticker_symbol_table_empty, ticker_symbol_not_in_table
from ORMLogic import api_call_to_json, ORM_services

class test_ORM_services_python_file(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()