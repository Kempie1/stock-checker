#External
from decouple import config
import psycopg2
import psycopg2.extras
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#Internal
from declarative import Stock, Base


class ORM_services:
        def __init__(self):
                engine = create_engine(config("DB_URL"))
                Base.metadata.bind = engine
                DBSession = sessionmaker()
                DBSession.bind = engine
                self.session = DBSession()

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
                ticker_symbol_table= []
                for ticker_symbol in self.session.query(Stock.ticker_symbol):
                        ticker_symbol_table.append(ticker_symbol[0])
                
                return ticker_symbol_table

        def checking_if_ticker_exists(self, ticker_symbol, ticker_table_list):
                print(ticker_symbol)
                print(ticker_table_list)
                if ticker_table_list == ['REALCASE']:
                        ticker_table_list = self.get_ticker_table_list()
                print(ticker_table_list)
                        
                already_exist = False

                if not ticker_table_list:
                        return already_exist

                for i in ticker_table_list:
                        if ticker_symbol == i:
                                already_exist = True

                return already_exist
