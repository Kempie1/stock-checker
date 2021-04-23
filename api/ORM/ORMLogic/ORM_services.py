from decouple import config
import psycopg2
import psycopg2.extras
import requests

class ORM_services:
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
        
        def checking_if_ticker_exists(self, ticker_symbol, ticker_symbol_table):
                for i in range(len(ticker_symbol_table)):
                        if ticker_symbol == ticker_symbol_table[i]:
                                print("This Ticker is already existing in the Database")
                                already_exist = True
                                return already_exist
                
                for i in range(len(ticker_symbol_table)):
                        if ticker_symbol != str(ticker_symbol_table[i]):
                                print("This Ticker does not yet exists in the Database")
                                already_exist = False
                
                if len(ticker_symbol_table) == 0:
                        print("There is nothing in the ticker_symbol Table")
                        already_exist = False
                
                return already_exist

#services = ORM_services()
#services.checking_if_ticker_exists(['TSLA'],[['CSV'], ['AAPL'], ['TSLA']])