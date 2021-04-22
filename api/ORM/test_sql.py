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
sys.path.insert(1, '/Users/maximilianhues/Documents/CODE/stock-checker/api/ORM')
from services import get_todos, get_uncompleted_todos
from constants import ticker_symbol_for_testing, ticker_symbol_for_request, ticker_symbol_table_full, ticker_symbol_table_empty, ticker_symbol_not_in_table
from json_to_server import open_json_file


class test_Sql_Integration(unittest.TestCase):
    def integration(self):
        DB_HOST = config('DB_HOST')
        DB_NAME = config('DB_NAME')
        DB_USER = config('DB_USER')
        DB_PASS = config('DB_PASS')

        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        self.assertIsNotNone(conn)
        conn.close()

test_sql_integration = test_Sql_Integration()
test_sql_integration.integration()

class test_Sql_python_file(unittest.TestCase):
    def test_open_json_file(self):
        stock_data = open_json_file()


test_sql_python_file = test_Sql_python_file()
test_sql_python_file.test_open_json_file()