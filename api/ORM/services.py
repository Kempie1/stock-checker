#External
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin
import requests
import os
import unittest
import psycopg2
import psycopg2.extras
#Internal
from constants import ticker_symbol_for_testing
from decouple import config

def real_api_request():
        ticker_symbol = ticker_symbol_for_testing
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-statistics"
        querystring = {"symbol": ticker_symbol,"region":"US"}
        headers = {
        'x-rapidapi-key': "92e0efc621msh368787aa782ea71p111f83jsn3acbf2f81995",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.ok:
            return response
        else:
            return None

def real_sql_request():
    DB_HOST = config('DB_HOST')
    DB_NAME = config('DB_NAME')
    DB_USER = config('DB_USER')
    DB_PASS = config('DB_PASS')

    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

    return conn