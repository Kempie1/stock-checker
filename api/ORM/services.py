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
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config
import sys
sys.path.append(config('ORM'))
sys.path.append(config('ORMLogic'))
sys.path.append(config('MockFolder'))
sys.path.append(config('APIFOLDER'))
#Internal
from declarative import Stock, Base
from constants import ticker_symbol_for_testing
def mock_api_request():
    response = requests.get("http://127.0.0.1:5000/json")
    return response

def mock_third_party_api_request():
    response = requests.get("http://127.0.0.1:4000/json")
    return response

def real_api_request():
    response = requests.get(f"https://stockcheckerdb.herokuapp.com/getst/?ticker={ticker_symbol_for_testing}")
    return response

def real_third_party_api_request():
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
    #This is creating an engine connected to the Database URL
    #engine = create_engine(config("DB_URL"))
    #Base.metadata.bind = engine
    #DBSession = sessionmaker()
    #DBSession.bind = engine
    #session = DBSession()
   # engine = create_engine(config("DB_URL"))
    #Base.metadata.bind = engine
    #session = sessionmaker(bind=engine)
    #session.query(Stock).all()
    print("")

mock_api_request