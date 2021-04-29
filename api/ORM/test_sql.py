import requests
import json
import psycopg2
import psycopg2.extras
import json
import jsonpath
import unittest
import os
import sys
from decouple import config
#This is needed to have acess to the ORM folder
sys.path.append('/Users/maximilianhues/Documents/CODE/stock-checker/api/ORM/ORMLogic')
from services import real_api_request, real_sql_request
from constants import ticker_symbol_for_testing, ticker_symbol_for_request, ticker_symbol_table_full, ticker_symbol_table_empty, ticker_symbol_not_in_table
#EXTERNAL
from ORMLogic import json_to_server

class test_Sql_Integration(unittest.TestCase):
    def test_sql_connection(self):
        #Act
        conn = real_sql_request()
        #Assert
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute('''
                    SELECT column_name
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE column_name LIKE 'ticker_symbol';
                ''')
                    select_column_ticker_symbol = cur.fetchall()
        self.assertEqual(select_column_ticker_symbol[0], ['ticker_symbol'])

#if __name__ == '__main__':
 #   unittest.main()

#test_sql_integration = test_Sql_Integration()
#test_sql_integration.integration()

class _Sql_python_file(unittest.TestCase):
    def _open_json_file(self):
        #Arrange
        server_to_json = json_to_server.Json_to_server()
        #Act
        stock_data = server_to_json.open_json_file("ORM/teststock.json")
        
        #Assert
        print(stock_data('get-statistics'))
#if __name__ == '__main__':
#    unittest.main()
#test_Sql_python_file = test_Sql_python_file()
#test_Sql_python_file.test_open_json_file()