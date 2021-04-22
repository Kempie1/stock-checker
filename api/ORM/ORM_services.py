from decouple import config
import psycopg2
import psycopg2.extras
import requests


def connecting_to_server():
        DB_HOST = config('DB_HOST')
        DB_NAME = config('DB_NAME')
        DB_USER = config('DB_USER')
        DB_PASS = config('DB_PASS')
        
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        return conn

def api_request(ticker_symbol, request):
    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/{request}"   
    querystring = {"symbol": ticker_symbol,"region":"US"}
    headers = {
    'x-rapidapi-key': config('APIKEY'),
    'x-rapidapi-host': config('APIHOST')
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

