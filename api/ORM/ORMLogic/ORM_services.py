from decouple import config
import psycopg2
import psycopg2.extras
import requests

class ORM_services:
        def connecting_to_server(self):
                DB_HOST = config('DB_HOST')
                DB_NAME = config('DB_NAME')
                DB_USER = config('DB_USER')
                DB_PASS = config('DB_PASS')
                
                conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
                return conn

        def api_request(self, request, ticker_symbol):
                url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/{request}"   
                querystring = {"symbol": ticker_symbol,"region":"US"}
                headers = {
                'x-rapidapi-key': config('APIKEY'),
                'x-rapidapi-host': config('APIHOST')
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                return response.text

        def get_ticker_table_list(self):
                conn = self.connecting_to_server()
                with conn: 
                        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                                cur.execute("SELECT stock.ticker_symbol FROM stock")
                                ticker_symbol_table = cur.fetchall()
                        return ticker_symbol_table

        def checking_if_ticker_exists(self, ticker_symbol, ticker_table_list):
                if ticker_table_list == ['REALCASE']:
                        ticker_table_list = self.get_ticker_table_list()
                        
                already_exist = False

                if not ticker_table_list:
                        print("There is nothing in the ticker_table_list Table")
                        return already_exist

                for i in ticker_table_list:
                        if ticker_symbol == i:
                                print(f"{i} already exists in the Database")
                                already_exist = True

                if not already_exist:
                        print(f"{ticker_symbol} does not yet exist in the Database")
                return already_exist

#services = ORM_services()
#services.checking_if_ticker_exists(['TSLA'], ['REALCASE'])